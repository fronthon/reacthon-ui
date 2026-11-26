from browser import window
from javascript import Date, Math, NULL
from reacthon import memo, use_effect, use_memo, use_ref, use_state
from utils import cn
from button import Button
from card import Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle

multiband_defaults = {
    "bands": 5,
    "loPass": 100,
    "hiPass": 600,
    "updateInterval": 32,
    "analyserOptions": {"fftSize": 2048},
}


def normalize_db(value):
    if value == -window.Infinity:
        return 0
    min_db = -100
    max_db = -10
    db = 1 - Math.max(min_db, Math.min(max_db, value)) * -1 / 100
    return Math.sqrt(db)


def create_audio_analyser(media_stream, options={}):
    audio_context = (window.AudioContext or window["webkitAudioContext"]).new()
    source = audio_context.createMediaStreamSource(media_stream)
    analyser = audio_context.createAnalyser()

    if options.get("fftSize"):
        analyser.fftSize = options.get("fftSize")
    if options.get("smoothingTimeConstant") is not None:
        analyser.smoothingTimeConstant = options.get("smoothingTimeConstant")
    if options.get("minDecibels") is not None:
        analyser.minDecibels = options.get("minDecibels")
    if options.get("maxDecibels") is not None:
        analyser.maxDecibels = options.get("maxDecibels")

    source.connect(analyser)

    def cleanup():
        source.disconnect()
        audio_context.close()

    return {"analyser": analyser, "audioContext": audio_context, "cleanup": cleanup}


def use_multiband_volume(media_stream, options={}):
    bands = options.get("bands") if options.get("bands") not in (None, NULL) else multiband_defaults.get("bands")
    if bands in (None, NULL):
        bands = 5
    lo_pass = options.get("loPass") if options.get("loPass") not in (None, NULL) else multiband_defaults.get("loPass")
    if lo_pass in (None, NULL):
        lo_pass = 100
    hi_pass = options.get("hiPass") if options.get("hiPass") not in (None, NULL) else multiband_defaults.get("hiPass")
    if hi_pass in (None, NULL):
        hi_pass = 600
    update_interval = options.get("updateInterval") if options.get("updateInterval") not in (None, NULL) else multiband_defaults.get("updateInterval")
    if update_interval in (None, NULL):
        update_interval = 32
    fft_size = options.get("analyserOptions").get("fftSize") if options.get("analyserOptions") else None
    if fft_size in (None, NULL):
        fft_size = multiband_defaults.get("analyserOptions").get("fftSize") if multiband_defaults.get("analyserOptions") else None
    smoothing_time_constant = options.get("analyserOptions").get("smoothingTimeConstant") if options.get("analyserOptions") else None
    if smoothing_time_constant in (None, NULL):
        smoothing_time_constant = multiband_defaults.get("analyserOptions").get("smoothingTimeConstant") if multiband_defaults.get("analyserOptions") else None
    min_decibels = options.get("analyserOptions").get("minDecibels") if options.get("analyserOptions") else None
    if min_decibels in (None, NULL):
        min_decibels = multiband_defaults.get("analyserOptions").get("minDecibels") if multiband_defaults.get("analyserOptions") else None
    max_decibels = options.get("analyserOptions").get("maxDecibels") if options.get("analyserOptions") else None
    if max_decibels in (None, NULL):
        max_decibels = multiband_defaults.get("analyserOptions").get("maxDecibels") if multiband_defaults.get("analyserOptions") else None

    frequency_bands, set_frequency_bands = use_state(lambda: window.Array.new(bands).fill(0))
    bands_ref = use_ref(window.Array.new(bands).fill(0))
    frame_id = use_ref(None)

    def effect():
        if not media_stream:
            empty_bands = window.Array.new(bands).fill(0)
            bands_ref.current = empty_bands
            set_frequency_bands(empty_bands)
            return

        create_audio_analyser_2 = create_audio_analyser(media_stream, {"fftSize": fft_size, "smoothingTimeConstant": smoothing_time_constant, "minDecibels": min_decibels, "maxDecibels": max_decibels})
        analyser, cleanup = create_audio_analyser_2.get("analyser"), create_audio_analyser_2.get("cleanup")

        buffer_length = analyser.frequencyBinCount
        data_array = window.Float32Array.new(buffer_length)
        slice_start = lo_pass
        slice_end = hi_pass
        slice_length = slice_end - slice_start
        chunk_size = Math.ceil(slice_length / bands)

        last_update = 0

        def update_volume(timestamp):
            nonlocal last_update
            if timestamp - last_update >= update_interval:
                analyser.getFloatFrequencyData(data_array)

                chunks = window.Array.new(bands)

                for i in range(bands):
                    sum_ = 0
                    count = 0
                    start_idx = slice_start + i * chunk_size
                    end_idx = Math.min(slice_start + (i + 1) * chunk_size, slice_end)

                    for j in range(start_idx, end_idx):
                        sum_ += normalize_db(data_array[j])
                        count += 1

                    chunks[i] = sum_ / count if count > 0 else 0

                has_changed = False
                for i in range(len(chunks)):
                    if Math.abs(chunks[i] - bands_ref.current[i]) > 0.01:
                        has_changed = True
                        break

                if has_changed:
                    bands_ref.current = chunks
                    set_frequency_bands(chunks)

                last_update = timestamp

            frame_id.current = window.requestAnimationFrame(update_volume)

        frame_id.current = window.requestAnimationFrame(update_volume)

        def cleanup_2():
            cleanup()
            if frame_id.current:
                window.cancelAnimationFrame(frame_id.current)

        return cleanup_2

    use_effect(
        effect,
        [bands, fft_size, hi_pass, lo_pass, max_decibels, media_stream, min_decibels, smoothing_time_constant, update_interval],
    )

    return frequency_bands


def generate_connecting_sequence_bar(columns):
    seq = []
    for x in range(columns):
        seq.append([x, columns - 1 - x])
    return seq


def generate_listening_sequence_bar(columns):
    center = Math.floor(columns / 2)
    no_index = -1
    return [[center], [no_index]]


def use_bar_animator(state, columns, interval):
    index_ref = use_ref(0)
    current_frame, set_current_frame = use_state([])
    animation_frame_id = use_ref(NULL)

    def sequence():
        if state == "thinking" or state == "listening":
            return generate_listening_sequence_bar(columns)
        elif state == "connecting" or state == "initializing":
            return generate_connecting_sequence_bar(columns)
        elif state is None or state == "speaking":
            return [[idx for idx, _ in enumerate(window.Array.new(columns).fill(0))]]
        else:
            return [[]]

    sequence = use_memo(sequence, [state, columns])

    def effect():
        index_ref.current = 0
        set_current_frame(sequence[0] or [])

    use_effect(effect, [sequence])

    def effect_2():
        start_time = window.performance.now()

        def animate(time):
            nonlocal start_time
            time_elapsed = time - start_time

            if time_elapsed >= interval:
                index_ref.current = (index_ref.current + 1) % len(sequence)
                set_current_frame(sequence[index_ref.current] or [])
                start_time = time

            animation_frame_id.current = window.requestAnimationFrame(animate)

        animation_frame_id.current = window.requestAnimationFrame(animate)

        def cleanup():
            if animation_frame_id.current is not NULL:
                window.cancelAnimationFrame(animation_frame_id.current)

        return cleanup

    use_effect(effect_2, [interval, sequence])

    return current_frame


@memo
def Bar(heightPct=None, isHighlighted=None, state=None, **_):
    return t"""
        <div
            data-highlighted={isHighlighted}
            class={cn(
                "max-w-[12px] min-w-[8px] flex-1 transition-all duration-150",
                "rounded-full",
                "bg-border data-[highlighted=true]:bg-chart-3",
                state == "speaking" and "bg-chart-3",
                state == "thinking" and isHighlighted and "animate-pulse",
            )}
            style={ {
                "height": f"{heightPct}%",
                "animationDuration": "300ms" if state == "thinking" else None,
            } }
        />
    """


Bar.displayName = "Bar"


def BarVisualizerComponent(state=None, barCount=15, mediaStream=None, minHeight=20, maxHeight=100, demo=False, centerAlign=False, className=None, style=None, ref=None, **props):
    real_volume_bands = use_multiband_volume(mediaStream, {"bands": barCount, "loPass": 100, "hiPass": 200})

    fake_volume_bands_ref = use_ref(window.Array.new(barCount).fill(0.2))
    fake_volume_bands, set_fake_volume_bands = use_state(lambda: window.Array.new(barCount).fill(0.2))
    fake_animation_ref = use_ref(None)

    def effect():
        if not demo:
            return

        if state != "speaking" and state != "listening":
            bands = window.Array.new(barCount).fill(0.2)
            fake_volume_bands_ref.current = bands
            set_fake_volume_bands(bands)
            return

        last_update = 0
        update_interval = 50
        start_time = Date.now() / 1000

        def update_fake_volume(timestamp):
            nonlocal last_update
            if timestamp - last_update >= update_interval:
                time = Date.now() / 1000 - start_time
                new_bands = window.Array.new(barCount)

                for i in range(barCount):
                    wave_offset = i * 0.5
                    base_volume = Math.sin(time * 2 + wave_offset) * 0.3 + 0.5
                    random_noise = Math.random() * 0.2
                    new_bands[i] = Math.max(0.1, Math.min(1, base_volume + random_noise))

                has_changed = False
                for i in range(barCount):
                    if Math.abs(new_bands[i] - fake_volume_bands_ref.current[i]) > 0.05:
                        has_changed = True
                        break

                if has_changed:
                    fake_volume_bands_ref.current = new_bands
                    set_fake_volume_bands(new_bands)

                last_update = timestamp

            fake_animation_ref.current = window.requestAnimationFrame(update_fake_volume)

        fake_animation_ref.current = window.requestAnimationFrame(update_fake_volume)

        def cleanup():
            if fake_animation_ref.current:
                window.cancelAnimationFrame(fake_animation_ref.current)

        return cleanup

    use_effect(effect, [demo, state, barCount])

    volume_bands = use_memo(
        lambda: fake_volume_bands if demo else real_volume_bands,
        [demo, fake_volume_bands, real_volume_bands],
    )

    highlighted_indices = use_bar_animator(
        state,
        barCount,
        2000 / barCount if state == "connecting" else 150 if state == "thinking" else 500 if state == "listening" else 1000,
    )

    def render_volume(volume, index):
        height_pct = Math.min(maxHeight, Math.max(minHeight, volume * 100 + 5))
        is_highlighted = index in highlighted_indices
        if is_highlighted in (None, NULL):
            is_highlighted = False

        return t"<{Bar} key={index} heightPct={height_pct} isHighlighted={is_highlighted} state={state} />"

    return t"""
        <div
            ref={ref}
            data-state={state}
            class={cn(
                "relative flex justify-center gap-1.5",
                "items-center" if centerAlign else "items-end",
                "h-32 w-full overflow-hidden rounded-lg bg-muted p-4",
                className,
            )}
            style={ {
                **(style or {}),
            } }
            ...{props}
        >
            {[render_volume(volume, index) for index, volume in enumerate(volume_bands)]}
        </div>
    """


BarVisualizerComponent.displayName = "BarVisualizerComponent"

BarVisualizer = memo(
    BarVisualizerComponent,
    lambda prev_props, next_props: prev_props.get("state") == next_props.get("state") and prev_props.get("barCount") == next_props.get("barCount") and prev_props.get("mediaStream") == next_props.get("mediaStream") and prev_props.get("minHeight") == next_props.get("minHeight") and prev_props.get("maxHeight") == next_props.get("maxHeight") and prev_props.get("demo") == next_props.get("demo") and prev_props.get("centerAlign") == next_props.get("centerAlign") and prev_props.get("className") == next_props.get("className") and window.JSON.stringify(prev_props.get("style")) == window.JSON.stringify(next_props.get("style")),
)

BarVisualizer.displayName = "BarVisualizer"


def BarVisualizerCard():
    state, set_state = use_state("speaking")

    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Audio Frequency Visualizer</{CardTitle}>
                <{CardDescription}>
                    Real-time frequency band visualization with animated state transitions
                </{CardDescription}>
            </{CardHeader}>
            <{CardContent}>
                <{BarVisualizer}
                    state={state}
                    demo={True}
                    barCount={20}
                    minHeight={15}
                    maxHeight={90}
                    class="h-40 max-w-full"
                />
            </{CardContent}>
            <{CardFooter} class="gap-2">
                <{Button}
                    size="sm"
                    variant={"default" if state == "connecting" else "outline"}
                    onClick={(lambda: set_state("connecting"))}
                >
                    Connecting
                </{Button}>
                <{Button}
                    size="sm"
                    variant={"default" if state == "listening" else "outline"}
                    onClick={(lambda: set_state("listening"))}
                >
                    Listening
                </{Button}>
                <{Button}
                    size="sm"
                    variant={"default" if state == "speaking" else "outline"}
                    onClick={(lambda: set_state("speaking"))}
                >
                    Speaking
                </{Button}>
            </{CardFooter}>
        </{Card}>
    """
