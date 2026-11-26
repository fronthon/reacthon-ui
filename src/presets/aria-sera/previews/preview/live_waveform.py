from browser import aio, window
from javascript import Math, NULL
from reacthon import use_effect, use_ref, use_state
from utils import cn
from button import Button
from card import Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle


def LiveWaveform(active=False, processing=False, deviceId=None, barWidth=3, barGap=1, barRadius=1.5, barColor=None, fadeEdges=True, fadeWidth=24, barHeight=4, height=64, sensitivity=1, smoothingTimeConstant=0.8, fftSize=256, historySize=60, updateRate=30, mode="static", onError=None, onStreamReady=None, onStreamEnd=None, className=None, **props):
    base_bar_height = barHeight

    canvas_ref = use_ref(NULL)
    container_ref = use_ref(NULL)
    history_ref = use_ref([])
    analyser_ref = use_ref(NULL)
    audio_context_ref = use_ref(NULL)
    stream_ref = use_ref(NULL)
    animation_ref = use_ref(0)
    last_update_ref = use_ref(0)
    processing_animation_ref = use_ref(NULL)
    last_active_data_ref = use_ref([])
    transition_progress_ref = use_ref(0)
    static_bars_ref = use_ref([])
    needs_redraw_ref = use_ref(True)
    gradient_cache_ref = use_ref(NULL)
    last_width_ref = use_ref(0)
    height_style = f"{height}px" if isinstance(height, (int, float)) else height

    # Handle canvas resizing.
    def effect():
        canvas = canvas_ref.current
        container = container_ref.current
        if not canvas or not container:
            return

        def callback():
            rect = container.getBoundingClientRect()
            dpr = window.devicePixelRatio or 1
            window.Reflect.set(canvas, "width", rect.width * dpr)
            window.Reflect.set(canvas, "height", rect.height * dpr)
            canvas.style.width = f"{rect.width}px"
            canvas.style.height = f"{rect.height}px"
            ctx = canvas.getContext("2d")
            if ctx:
                ctx.scale(dpr, dpr)
            gradient_cache_ref.current = NULL
            last_width_ref.current = rect.width
            needs_redraw_ref.current = True

        resize_observer = window.ResizeObserver.new(callback)

        resize_observer.observe(container)
        return lambda: resize_observer.disconnect()

    use_effect(effect, [])

    def effect_2():
        if processing and not active:
            time = 0
            transition_progress_ref.current = 0

            def animate_processing():
                nonlocal time
                time += 0.03
                transition_progress_ref.current = Math.min(1, transition_progress_ref.current + 0.02)
                processing_data = []
                bar_count = Math.floor(
                    ((container_ref.current.getBoundingClientRect().width if container_ref.current else None) or 200) / (barWidth + barGap),
                )
                if mode == "static":
                    half_count = Math.floor(bar_count / 2)
                    for i in range(bar_count):
                        normalized_position = (i - half_count) / half_count
                        center_weight = 1 - Math.abs(normalized_position) * 0.4
                        wave1 = Math.sin(time * 1.5 + normalized_position * 3) * 0.25
                        wave2 = Math.sin(time * 0.8 - normalized_position * 2) * 0.2
                        wave3 = Math.cos(time * 2 + normalized_position) * 0.15
                        combined_wave = wave1 + wave2 + wave3
                        processing_value = (0.2 + combined_wave) * center_weight
                        final_value = processing_value
                        if len(last_active_data_ref.current) > 0 and transition_progress_ref.current < 1:
                            last_data_index = Math.min(i, len(last_active_data_ref.current) - 1)
                            last_value = last_active_data_ref.current[last_data_index] or 0
                            final_value = last_value * (1 - transition_progress_ref.current) + processing_value * transition_progress_ref.current
                        processing_data.append(Math.max(0.05, Math.min(1, final_value)))
                else:
                    for i in range(bar_count):
                        normalized_position = (i - bar_count / 2) / (bar_count / 2)
                        center_weight = 1 - Math.abs(normalized_position) * 0.4
                        wave1 = Math.sin(time * 1.5 + i * 0.15) * 0.25
                        wave2 = Math.sin(time * 0.8 - i * 0.1) * 0.2
                        wave3 = Math.cos(time * 2 + i * 0.05) * 0.15
                        combined_wave = wave1 + wave2 + wave3
                        processing_value = (0.2 + combined_wave) * center_weight
                        final_value = processing_value
                        if len(last_active_data_ref.current) > 0 and transition_progress_ref.current < 1:
                            last_data_index = Math.floor(i / bar_count * len(last_active_data_ref.current))
                            last_value = last_active_data_ref.current[last_data_index] or 0
                            final_value = last_value * (1 - transition_progress_ref.current) + processing_value * transition_progress_ref.current
                        processing_data.append(Math.max(0.05, Math.min(1, final_value)))
                if mode == "static":
                    static_bars_ref.current = processing_data
                else:
                    history_ref.current = processing_data
                needs_redraw_ref.current = True
                processing_animation_ref.current = window.requestAnimationFrame(animate_processing)

            animate_processing()

            def cleanup():
                if processing_animation_ref.current:
                    window.cancelAnimationFrame(processing_animation_ref.current)

            return cleanup
        elif not active and not processing:
            has_data = len(static_bars_ref.current) > 0 if mode == "static" else len(history_ref.current) > 0
            if has_data:
                fade_progress = 0

                def fade_to_idle():
                    nonlocal fade_progress
                    fade_progress += 0.03
                    if fade_progress < 1:
                        if mode == "static":
                            static_bars_ref.current = [value * (1 - fade_progress) for value in static_bars_ref.current]
                        else:
                            history_ref.current = [value * (1 - fade_progress) for value in history_ref.current]
                        needs_redraw_ref.current = True
                        window.requestAnimationFrame(fade_to_idle)
                    else:
                        if mode == "static":
                            static_bars_ref.current = []
                        else:
                            history_ref.current = []

                fade_to_idle()

    use_effect(effect_2, [processing, active, barWidth, barGap, mode])

    # Handle microphone setup and teardown.
    def effect_3():
        if not active:
            if stream_ref.current:
                for track in stream_ref.current.getTracks():
                    track.stop()
                stream_ref.current = NULL
                if onStreamEnd:
                    onStreamEnd()
            if audio_context_ref.current and audio_context_ref.current.state != "closed":
                audio_context_ref.current.close()
                audio_context_ref.current = NULL
            if animation_ref.current:
                window.cancelAnimationFrame(animation_ref.current)
                animation_ref.current = 0
            return
        async def setup_microphone():
            try:
                stream = await window.navigator.mediaDevices.getUserMedia({"audio": {"deviceId": {"exact": deviceId}, "echoCancellation": True, "noiseSuppression": True, "autoGainControl": True} if deviceId else {"echoCancellation": True, "noiseSuppression": True, "autoGainControl": True}})
                stream_ref.current = stream
                if onStreamReady:
                    onStreamReady(stream)
                AudioContextConstructor = window.AudioContext or window["webkitAudioContext"]
                audio_context = AudioContextConstructor.new()
                analyser = audio_context.createAnalyser()
                analyser.fftSize = fftSize
                analyser.smoothingTimeConstant = smoothingTimeConstant
                source = audio_context.createMediaStreamSource(stream)
                source.connect(analyser)
                audio_context_ref.current = audio_context
                analyser_ref.current = analyser
                history_ref.current = []
            except Exception as error:
                if onError:
                    onError(error)
        aio.run(setup_microphone())

        def cleanup():
            if stream_ref.current:
                for track in stream_ref.current.getTracks():
                    track.stop()
                stream_ref.current = NULL
                if onStreamEnd:
                    onStreamEnd()
            if audio_context_ref.current and audio_context_ref.current.state != "closed":
                audio_context_ref.current.close()
                audio_context_ref.current = NULL
            if animation_ref.current:
                window.cancelAnimationFrame(animation_ref.current)
                animation_ref.current = 0

        return cleanup

    use_effect(effect_3, [active, deviceId, fftSize, smoothingTimeConstant, onError, onStreamReady, onStreamEnd])

    # Animation loop.
    def effect_4():
        canvas = canvas_ref.current
        if not canvas:
            return
        ctx = canvas.getContext("2d")
        if not ctx:
            return
        raf_id = None

        def animate(current_time):
            nonlocal raf_id
            rect = canvas.getBoundingClientRect()
            if active and current_time - last_update_ref.current > updateRate:
                last_update_ref.current = current_time
                if analyser_ref.current:
                    data_array = window.Uint8Array.new(analyser_ref.current.frequencyBinCount)
                    analyser_ref.current.getByteFrequencyData(data_array)
                    if mode == "static":
                        start_freq = Math.floor(data_array.length * 0.05)
                        end_freq = Math.floor(data_array.length * 0.4)
                        relevant_data = data_array.slice(start_freq, end_freq)
                        bar_count = Math.floor(rect.width / (barWidth + barGap))
                        half_count = Math.floor(bar_count / 2)
                        new_bars = []
                        for i in range(half_count - 1, -1, -1):
                            data_index = Math.floor(i / half_count * relevant_data.length)
                            value = Math.min(1, relevant_data[data_index] / 255 * sensitivity)
                            new_bars.append(Math.max(0.05, value))
                        for i in range(half_count):
                            data_index = Math.floor(i / half_count * relevant_data.length)
                            value = Math.min(1, relevant_data[data_index] / 255 * sensitivity)
                            new_bars.append(Math.max(0.05, value))
                        static_bars_ref.current = new_bars
                        last_active_data_ref.current = new_bars
                    else:
                        sum_ = 0
                        start_freq = Math.floor(data_array.length * 0.05)
                        end_freq = Math.floor(data_array.length * 0.4)
                        relevant_data = data_array.slice(start_freq, end_freq)
                        for i in range(relevant_data.length):
                            sum_ += relevant_data[i]
                        average = sum_ / relevant_data.length / 255 * sensitivity
                        history_ref.current.append(Math.min(1, Math.max(0.05, average)))
                        last_active_data_ref.current = list(history_ref.current)
                        if len(history_ref.current) > historySize:
                            history_ref.current.shift()
                    needs_redraw_ref.current = True
            if not needs_redraw_ref.current and not active:
                raf_id = window.requestAnimationFrame(animate)
                return
            needs_redraw_ref.current = active
            ctx.clearRect(0, 0, rect.width, rect.height)

            def callback():
                style = window.getComputedStyle(canvas)
                color = style.color
                return color or "#000"

            computed_bar_color = barColor or callback()

            step = barWidth + barGap
            bar_count = Math.floor(rect.width / step)
            center_y = rect.height / 2
            if mode == "static":
                data_to_render = static_bars_ref.current if processing else static_bars_ref.current if active else static_bars_ref.current if len(static_bars_ref.current) > 0 else []
                for i in range(min(bar_count, len(data_to_render))):
                    value = data_to_render[i] or 0.1
                    x = i * step
                    bh = Math.max(base_bar_height, value * rect.height * 0.8)
                    y = center_y - bh / 2
                    ctx.fillStyle = computed_bar_color
                    ctx.globalAlpha = 0.4 + value * 0.6
                    if barRadius > 0:
                        ctx.beginPath()
                        ctx.roundRect(x, y, barWidth, bh, barRadius)
                        ctx.fill()
                    else:
                        ctx.fillRect(x, y, barWidth, bh)
            else:
                for i in range(min(bar_count, len(history_ref.current))):
                    data_index = len(history_ref.current) - 1 - i
                    value = history_ref.current[data_index] or 0.1
                    x = rect.width - (i + 1) * step
                    bh = Math.max(base_bar_height, value * rect.height * 0.8)
                    y = center_y - bh / 2
                    ctx.fillStyle = computed_bar_color
                    ctx.globalAlpha = 0.4 + value * 0.6
                    if barRadius > 0:
                        ctx.beginPath()
                        ctx.roundRect(x, y, barWidth, bh, barRadius)
                        ctx.fill()
                    else:
                        ctx.fillRect(x, y, barWidth, bh)
            if fadeEdges and fadeWidth > 0 and rect.width > 0:
                if not gradient_cache_ref.current or last_width_ref.current != rect.width:
                    gradient = ctx.createLinearGradient(0, 0, rect.width, 0)
                    fade_percent = Math.min(0.3, fadeWidth / rect.width)
                    gradient.addColorStop(0, "rgba(255,255,255,1)")
                    gradient.addColorStop(fade_percent, "rgba(255,255,255,0)")
                    gradient.addColorStop(1 - fade_percent, "rgba(255,255,255,0)")
                    gradient.addColorStop(1, "rgba(255,255,255,1)")
                    gradient_cache_ref.current = gradient
                    last_width_ref.current = rect.width
                ctx.globalCompositeOperation = "destination-out"
                ctx.fillStyle = gradient_cache_ref.current
                ctx.fillRect(0, 0, rect.width, rect.height)
                ctx.globalCompositeOperation = "source-over"
            ctx.globalAlpha = 1
            raf_id = window.requestAnimationFrame(animate)

        raf_id = window.requestAnimationFrame(animate)

        def cleanup():
            if raf_id:
                window.cancelAnimationFrame(raf_id)

        return cleanup

    use_effect(
        effect_4,
        [active, processing, sensitivity, updateRate, historySize, barWidth, base_bar_height, barGap, barRadius, barColor, fadeEdges, fadeWidth, mode],
    )

    div = t"""
        <div class="absolute top-1/2 right-0 left-0 -translate-y-1/2 border-t-2 border-dotted border-muted-foreground/20" />
    """

    return t"""
        <div
            class={cn("relative h-full w-full", className)}
            ref={container_ref}
            style={ {
                "height": height_style,
            } }
            aria-label={"Live audio waveform" if active else "Processing audio" if processing else "Audio waveform idle"}
            role="img"
            ...{props}
        >
            {not active and not processing and div}
            <canvas class="block h-full w-full" ref={canvas_ref} aria-hidden="true" />
        </div>
    """


def LiveWaveformCard():
    active, set_active = use_state(False)
    processing, set_processing = use_state(True)
    mode, set_mode = use_state("static")

    def handle_toggle_active():
        set_active(not active)
        if not active:
            set_processing(False)

    def handle_toggle_processing():
        set_processing(not processing)
        if not processing:
            set_active(False)

    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Live Audio Waveform</{CardTitle}>
                <{CardDescription}>Real-time microphone input visualization with audio reactivity</{CardDescription}>
            </{CardHeader}>
            <{CardContent}>
                <{LiveWaveform}
                    active={active}
                    processing={processing}
                    height={80}
                    barWidth={3}
                    barGap={2}
                    mode={mode}
                    fadeEdges={True}
                    barColor="gray"
                    historySize={120}
                />
            </{CardContent}>
            <{CardFooter} class="gap-2">
                <{Button} size="sm" variant={"default" if active else "outline"} onClick={handle_toggle_active}>
                    {"Stop" if active else "Start"} Listening
                </{Button}>
                <{Button} size="sm" variant={"default" if processing else "outline"} onClick={handle_toggle_processing}>
                    {"Stop" if processing else "Start"} Processing
                </{Button}>
                <{Button}
                    size="sm"
                    variant="outline"
                    onClick={(lambda: set_mode("scrolling" if mode == "static" else "static"))}
                >
                    {"Static" if mode == "static" else "Scrolling"}
                </{Button}>
            </{CardFooter}>
        </{Card}>
    """
