from reacthon import use_state
from example import Example, ExampleWrapper
from badge import Badge
from checkbox import Checkbox
from field import Field, FieldContent, FieldDescription, FieldGroup, FieldLabel, FieldLegend, FieldSet, FieldTitle
from input import Input
from input_otp import InputOTP, InputOTPGroup, InputOTPSeparator, InputOTPSlot
from native_select import NativeSelect, NativeSelectOptGroup, NativeSelectOption
from radio_group import RadioGroup, RadioGroupItem
from select import Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue
from slider import Slider
from switch import Switch
from textarea import Textarea

__js__ = {"input-otp": ["REGEXP_ONLY_DIGITS"]}


def FieldExample():
    return t"""
        <{ExampleWrapper}>
            <{InputFields} />
            <{TextareaFields} />
            <{SelectFields} />
            <{CheckboxFields} />
            <{RadioFields} />
            <{SwitchFields} />
            <{SliderFields} />
            <{NativeSelectFields} />
            <{InputOTPFields} />
            <{HorizontalFields} />
        </{ExampleWrapper}>
    """


def InputFields():
    return t"""
        <{Example} title="Input Fields">
            <{FieldGroup}>
                <{Field}>
                    <{FieldLabel} for="input-basic">Basic Input</{FieldLabel}>
                    <{Input} id="input-basic" placeholder="Enter text" />
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="input-with-desc">Input with Description</{FieldLabel}>
                    <{Input} id="input-with-desc" placeholder="Enter your username" />
                    <{FieldDescription}>Choose a unique username for your account.</{FieldDescription}>
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="input-desc-first">Email Address</{FieldLabel}>
                    <{FieldDescription}>We'll never share your email with anyone.</{FieldDescription}>
                    <{Input} id="input-desc-first" type="email" placeholder="email@example.com" />
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="input-required">
                        Required Field <span class="text-destructive">*</span>
                    </{FieldLabel}>
                    <{Input} id="input-required" placeholder="This field is required" required />
                    <{FieldDescription}>This field must be filled out.</{FieldDescription}>
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="input-disabled">Disabled Input</{FieldLabel}>
                    <{Input} id="input-disabled" placeholder="Cannot edit" disabled />
                    <{FieldDescription}>This field is currently disabled.</{FieldDescription}>
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="input-badge">
                        Input with Badge{" "}
                        <{Badge} variant="secondary" class="ml-auto">Recommended</{Badge}>
                    </{FieldLabel}>
                    <{Input} id="input-badge" placeholder="Enter value" />
                </{Field}>
                <{Field} data-invalid>
                    <{FieldLabel} for="input-invalid">Invalid Input</{FieldLabel}>
                    <{Input} id="input-invalid" placeholder="This field has an error" aria-invalid />
                    <{FieldDescription}>This field contains validation errors.</{FieldDescription}>
                </{Field}>
                <{Field} data-disabled>
                    <{FieldLabel} for="input-disabled-field">Disabled Field</{FieldLabel}>
                    <{Input} id="input-disabled-field" placeholder="Cannot edit" disabled />
                    <{FieldDescription}>This field is currently disabled.</{FieldDescription}>
                </{Field}>
            </{FieldGroup}>
        </{Example}>
    """


def TextareaFields():
    return t"""
        <{Example} title="Textarea Fields">
            <{FieldGroup}>
                <{Field}>
                    <{FieldLabel} for="textarea-basic">Basic Textarea</{FieldLabel}>
                    <{Textarea} id="textarea-basic" placeholder="Enter your message" />
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="textarea-comments">Comments</{FieldLabel}>
                    <{Textarea} id="textarea-comments" placeholder="Share your thoughts..." class="min-h-[100px]" />
                    <{FieldDescription}>Maximum 500 characters allowed.</{FieldDescription}>
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="textarea-bio">Bio</{FieldLabel}>
                    <{FieldDescription}>Tell us about yourself in a few sentences.</{FieldDescription}>
                    <{Textarea} id="textarea-bio" placeholder="I am a..." class="min-h-[120px]" />
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="textarea-desc-after">Message</{FieldLabel}>
                    <{Textarea} id="textarea-desc-after" placeholder="Enter your message" />
                    <{FieldDescription}>Enter your message so it is long enough to test the layout.</{FieldDescription}>
                </{Field}>
                <{Field} data-invalid>
                    <{FieldLabel} for="textarea-invalid">Invalid Textarea</{FieldLabel}>
                    <{Textarea} id="textarea-invalid" placeholder="This field has an error" aria-invalid />
                    <{FieldDescription}>This field contains validation errors.</{FieldDescription}>
                </{Field}>
                <{Field} data-disabled>
                    <{FieldLabel} for="textarea-disabled-field">Disabled Field</{FieldLabel}>
                    <{Textarea} id="textarea-disabled-field" placeholder="Cannot edit" disabled />
                    <{FieldDescription}>This field is currently disabled.</{FieldDescription}>
                </{Field}>
            </{FieldGroup}>
        </{Example}>
    """


def SelectFields():
    basic_items = [
        {"label": "Option 1", "value": "option1"},
        {"label": "Option 2", "value": "option2"},
        {"label": "Option 3", "value": "option3"},
    ]
    country_items = [
        {"label": "United States", "value": "us"},
        {"label": "United Kingdom", "value": "uk"},
        {"label": "Canada", "value": "ca"},
    ]
    timezone_items = [
        {"label": "UTC", "value": "utc"},
        {"label": "Eastern Time", "value": "est"},
        {"label": "Pacific Time", "value": "pst"},
    ]
    invalid_items = [
        {"label": "Option 1", "value": "option1"},
        {"label": "Option 2", "value": "option2"},
        {"label": "Option 3", "value": "option3"},
    ]
    disabled_items = [
        {"label": "Option 1", "value": "option1"},
        {"label": "Option 2", "value": "option2"},
        {"label": "Option 3", "value": "option3"},
    ]

    return t"""
        <{Example} title="Select Fields">
            <{FieldGroup}>
                <{Field}>
                    <{FieldLabel} for="select-basic">Basic Select</{FieldLabel}>
                    <{Select} placeholder="Choose an option">
                        <{SelectTrigger} id="select-basic">
                            <{SelectValue} />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                {[t'''
                                    <{SelectItem}
                                        key={item["value"]}
                                        id={item["value"]}
                                    >
                                        {item["label"]}
                                    </{SelectItem}>
                                ''' for item in basic_items]}
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="select-country">Country</{FieldLabel}>
                    <{Select} placeholder="Select your country">
                        <{SelectTrigger} id="select-country">
                            <{SelectValue} />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                {[t'''
                                    <{SelectItem}
                                        key={item["value"]}
                                        id={item["value"]}
                                    >
                                        {item["label"]}
                                    </{SelectItem}>
                                ''' for item in country_items]}
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                    <{FieldDescription}>Select the country where you currently reside.</{FieldDescription}>
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="select-timezone">Timezone</{FieldLabel}>
                    <{FieldDescription}>Choose your local timezone for accurate scheduling.</{FieldDescription}>
                    <{Select} placeholder="Select timezone">
                        <{SelectTrigger} id="select-timezone">
                            <{SelectValue} />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                {[t'''
                                    <{SelectItem}
                                        key={item["value"]}
                                        id={item["value"]}
                                    >
                                        {item["label"]}
                                    </{SelectItem}>
                                ''' for item in timezone_items]}
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                </{Field}>
                <{Field} data-invalid>
                    <{FieldLabel} for="select-invalid">Invalid Select</{FieldLabel}>
                    <{Select} placeholder="This field has an error" isInvalid>
                        <{SelectTrigger} id="select-invalid">
                            <{SelectValue} />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                {[t'''
                                    <{SelectItem}
                                        key={item["value"]}
                                        id={item["value"]}
                                    >
                                        {item["label"]}
                                    </{SelectItem}>
                                ''' for item in invalid_items]}
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                    <{FieldDescription}>This field contains validation errors.</{FieldDescription}>
                </{Field}>
                <{Field} data-disabled>
                    <{FieldLabel} for="select-disabled-field">Disabled Field</{FieldLabel}>
                    <{Select} placeholder="Cannot select" isDisabled>
                        <{SelectTrigger} id="select-disabled-field">
                            <{SelectValue} />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                {[t'''
                                    <{SelectItem}
                                        key={item["value"]}
                                        id={item["value"]}
                                    >
                                        {item["label"]}
                                    </{SelectItem}>
                                ''' for item in disabled_items]}
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                    <{FieldDescription}>This field is currently disabled.</{FieldDescription}>
                </{Field}>
            </{FieldGroup}>
        </{Example}>
    """


def NativeSelectFields():
    return t"""
        <{Example} title="Native Select Fields">
            <{FieldGroup}>
                <{Field}>
                    <{FieldLabel} for="native-select-basic">Basic Native Select</{FieldLabel}>
                    <{NativeSelect} id="native-select-basic">
                        <{NativeSelectOption} value="">Choose an option</{NativeSelectOption}>
                        <{NativeSelectOption} value="option1">Option 1</{NativeSelectOption}>
                        <{NativeSelectOption} value="option2">Option 2</{NativeSelectOption}>
                        <{NativeSelectOption} value="option3">Option 3</{NativeSelectOption}>
                    </{NativeSelect}>
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="native-select-country">Country</{FieldLabel}>
                    <{NativeSelect} id="native-select-country">
                        <{NativeSelectOption} value="">Select your country</{NativeSelectOption}>
                        <{NativeSelectOption} value="us">United States</{NativeSelectOption}>
                        <{NativeSelectOption} value="uk">United Kingdom</{NativeSelectOption}>
                        <{NativeSelectOption} value="ca">Canada</{NativeSelectOption}>
                    </{NativeSelect}>
                    <{FieldDescription}>Select the country where you currently reside.</{FieldDescription}>
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="native-select-timezone">Timezone</{FieldLabel}>
                    <{FieldDescription}>Choose your local timezone for accurate scheduling.</{FieldDescription}>
                    <{NativeSelect} id="native-select-timezone">
                        <{NativeSelectOption} value="">Select timezone</{NativeSelectOption}>
                        <{NativeSelectOption} value="utc">UTC</{NativeSelectOption}>
                        <{NativeSelectOption} value="est">Eastern Time</{NativeSelectOption}>
                        <{NativeSelectOption} value="pst">Pacific Time</{NativeSelectOption}>
                    </{NativeSelect}>
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="native-select-grouped">Grouped Options</{FieldLabel}>
                    <{NativeSelect} id="native-select-grouped">
                        <{NativeSelectOption} value="">Select a region</{NativeSelectOption}>
                        <{NativeSelectOptGroup} label="North America">
                            <{NativeSelectOption} value="us">United States</{NativeSelectOption}>
                            <{NativeSelectOption} value="ca">Canada</{NativeSelectOption}>
                            <{NativeSelectOption} value="mx">Mexico</{NativeSelectOption}>
                        </{NativeSelectOptGroup}>
                        <{NativeSelectOptGroup} label="Europe">
                            <{NativeSelectOption} value="uk">United Kingdom</{NativeSelectOption}>
                            <{NativeSelectOption} value="fr">France</{NativeSelectOption}>
                            <{NativeSelectOption} value="de">Germany</{NativeSelectOption}>
                        </{NativeSelectOptGroup}>
                    </{NativeSelect}>
                    <{FieldDescription}>Native select with grouped options using optgroup.</{FieldDescription}>
                </{Field}>
                <{Field} data-invalid>
                    <{FieldLabel} for="native-select-invalid">Invalid Native Select</{FieldLabel}>
                    <{NativeSelect} id="native-select-invalid" aria-invalid>
                        <{NativeSelectOption} value="">This field has an error</{NativeSelectOption}>
                        <{NativeSelectOption} value="option1">Option 1</{NativeSelectOption}>
                        <{NativeSelectOption} value="option2">Option 2</{NativeSelectOption}>
                        <{NativeSelectOption} value="option3">Option 3</{NativeSelectOption}>
                    </{NativeSelect}>
                    <{FieldDescription}>This field contains validation errors.</{FieldDescription}>
                </{Field}>
                <{Field} data-disabled>
                    <{FieldLabel} for="native-select-disabled-field">Disabled Field</{FieldLabel}>
                    <{NativeSelect} id="native-select-disabled-field" disabled>
                        <{NativeSelectOption} value="">Cannot select</{NativeSelectOption}>
                        <{NativeSelectOption} value="option1">Option 1</{NativeSelectOption}>
                        <{NativeSelectOption} value="option2">Option 2</{NativeSelectOption}>
                        <{NativeSelectOption} value="option3">Option 3</{NativeSelectOption}>
                    </{NativeSelect}>
                    <{FieldDescription}>This field is currently disabled.</{FieldDescription}>
                </{Field}>
            </{FieldGroup}>
        </{Example}>
    """


def CheckboxFields():
    return t"""
        <{Example} title="Checkbox Fields">
            <{FieldGroup}>
                <{Field} orientation="horizontal">
                    <{Checkbox} id="checkbox-basic" defaultSelected />
                    <{FieldLabel} for="checkbox-basic">I agree to the terms and conditions</{FieldLabel}>
                </{Field}>
                <{Field} orientation="horizontal">
                    <{FieldLabel} for="checkbox-right">Accept terms and conditions</{FieldLabel}>
                    <{Checkbox} id="checkbox-right" />
                </{Field}>
                <{Field} orientation="horizontal">
                    <{Checkbox} id="checkbox-with-desc" />
                    <{FieldContent}>
                        <{FieldLabel} for="checkbox-with-desc">Subscribe to newsletter</{FieldLabel}>
                        <{FieldDescription}>
                            Receive weekly updates about new features and promotions.
                        </{FieldDescription}>
                    </{FieldContent}>
                </{Field}>
                <{FieldLabel} for="checkbox-with-title">
                    <{Field} orientation="horizontal">
                        <{Checkbox} id="checkbox-with-title" />
                        <{FieldContent}>
                            <{FieldTitle}>Enable Touch ID</{FieldTitle}>
                            <{FieldDescription}>Enable Touch ID to quickly unlock your device.</{FieldDescription}>
                        </{FieldContent}>
                    </{Field}>
                </{FieldLabel}>
                <{FieldSet}>
                    <{FieldLegend} variant="label">Preferences</{FieldLegend}>
                    <{FieldDescription}>Select all that apply to customize your experience.</{FieldDescription}>
                    <{FieldGroup} class="gap-3">
                        <{Field} orientation="horizontal">
                            <{Checkbox} id="pref-dark" />
                            <{FieldLabel} for="pref-dark">Dark mode</{FieldLabel}>
                        </{Field}>
                        <{Field} orientation="horizontal">
                            <{Checkbox} id="pref-compact" />
                            <{FieldLabel} for="pref-compact">Compact view</{FieldLabel}>
                        </{Field}>
                        <{Field} orientation="horizontal">
                            <{Checkbox} id="pref-notifications" />
                            <{FieldLabel} for="pref-notifications">Enable notifications</{FieldLabel}>
                        </{Field}>
                    </{FieldGroup}>
                </{FieldSet}>
                <{Field} data-invalid orientation="horizontal">
                    <{Checkbox} id="checkbox-invalid" isInvalid />
                    <{FieldLabel} for="checkbox-invalid">Invalid checkbox</{FieldLabel}>
                </{Field}>
                <{Field} data-disabled orientation="horizontal">
                    <{Checkbox} id="checkbox-disabled-field" isDisabled />
                    <{FieldLabel} for="checkbox-disabled-field">Disabled checkbox</{FieldLabel}>
                </{Field}>
            </{FieldGroup}>
        </{Example}>
    """


def RadioFields():
    return t"""
        <{Example} title="Radio Fields">
            <{FieldGroup}>
                <{FieldSet}>
                    <{FieldLegend} variant="label">Subscription Plan</{FieldLegend}>
                    <{RadioGroup} defaultValue="free">
                        <{Field} orientation="horizontal">
                            <{RadioGroupItem} value="free" id="radio-free" />
                            <{FieldLabel} for="radio-free">Free Plan</{FieldLabel}>
                        </{Field}>
                        <{Field} orientation="horizontal">
                            <{RadioGroupItem} value="pro" id="radio-pro" />
                            <{FieldLabel} for="radio-pro">Pro Plan</{FieldLabel}>
                        </{Field}>
                        <{Field} orientation="horizontal">
                            <{RadioGroupItem} value="enterprise" id="radio-enterprise" />
                            <{FieldLabel} for="radio-enterprise">Enterprise</{FieldLabel}>
                        </{Field}>
                    </{RadioGroup}>
                </{FieldSet}>
                <{FieldSet}>
                    <{FieldLegend} variant="label">Battery Level</{FieldLegend}>
                    <{FieldDescription}>Choose your preferred battery level.</{FieldDescription}>
                    <{RadioGroup}>
                        <{Field} orientation="horizontal">
                            <{RadioGroupItem} value="high" id="battery-high" />
                            <{FieldLabel} for="battery-high">High</{FieldLabel}>
                        </{Field}>
                        <{Field} orientation="horizontal">
                            <{RadioGroupItem} value="medium" id="battery-medium" />
                            <{FieldLabel} for="battery-medium">Medium</{FieldLabel}>
                        </{Field}>
                        <{Field} orientation="horizontal">
                            <{RadioGroupItem} value="low" id="battery-low" />
                            <{FieldLabel} for="battery-low">Low</{FieldLabel}>
                        </{Field}>
                    </{RadioGroup}>
                </{FieldSet}>
                <{RadioGroup} class="gap-6">
                    <{Field} orientation="horizontal">
                        <{RadioGroupItem} value="option1" id="radio-content-1" />
                        <{FieldContent}>
                            <{FieldLabel} for="radio-content-1">Enable Touch ID</{FieldLabel}>
                            <{FieldDescription}>Enable Touch ID to quickly unlock your device.</{FieldDescription}>
                        </{FieldContent}>
                    </{Field}>
                </{RadioGroup}>
                <{RadioGroup} class="gap-3">
                    <{FieldLabel} for="radio-title-1">
                        <{Field} orientation="horizontal">
                            <{RadioGroupItem} value="title1" id="radio-title-1" />
                            <{FieldContent}>
                                <{FieldTitle}>Enable Touch ID</{FieldTitle}>
                                <{FieldDescription}>Enable Touch ID to quickly unlock your device.</{FieldDescription}>
                            </{FieldContent}>
                        </{Field}>
                    </{FieldLabel}>
                </{RadioGroup}>
                <{FieldSet}>
                    <{FieldLegend} variant="label">Invalid Radio Group</{FieldLegend}>
                    <{RadioGroup} isInvalid>
                        <{Field} data-invalid orientation="horizontal">
                            <{RadioGroupItem} value="invalid1" id="radio-invalid-1" />
                            <{FieldLabel} for="radio-invalid-1">Invalid Option 1</{FieldLabel}>
                        </{Field}>
                        <{Field} data-invalid orientation="horizontal">
                            <{RadioGroupItem} value="invalid2" id="radio-invalid-2" />
                            <{FieldLabel} for="radio-invalid-2">Invalid Option 2</{FieldLabel}>
                        </{Field}>
                    </{RadioGroup}>
                </{FieldSet}>
                <{FieldSet}>
                    <{FieldLegend} variant="label">Disabled Radio Group</{FieldLegend}>
                    <{RadioGroup} isDisabled>
                        <{Field} data-disabled orientation="horizontal">
                            <{RadioGroupItem} value="disabled1" id="radio-disabled-1" />
                            <{FieldLabel} for="radio-disabled-1">Disabled Option 1</{FieldLabel}>
                        </{Field}>
                        <{Field} data-disabled orientation="horizontal">
                            <{RadioGroupItem} value="disabled2" id="radio-disabled-2" />
                            <{FieldLabel} for="radio-disabled-2">Disabled Option 2</{FieldLabel}>
                        </{Field}>
                    </{RadioGroup}>
                </{FieldSet}>
            </{FieldGroup}>
        </{Example}>
    """


def SwitchFields():
    return t"""
        <{Example} title="Switch Fields">
            <{FieldGroup}>
                <{Field} orientation="horizontal">
                    <{FieldContent}>
                        <{FieldLabel} for="switch-airplane">Airplane Mode</{FieldLabel}>
                        <{FieldDescription}>Turn on airplane mode to disable all connections.</{FieldDescription}>
                    </{FieldContent}>
                    <{Switch} id="switch-airplane" />
                </{Field}>
                <{Field} orientation="horizontal">
                    <{FieldLabel} for="switch-dark">Dark Mode</{FieldLabel}>
                    <{Switch} id="switch-dark" />
                </{Field}>
                <{Field} orientation="horizontal">
                    <{Switch} id="switch-marketing" />
                    <{FieldContent}>
                        <{FieldLabel} for="switch-marketing">Marketing Emails</{FieldLabel}>
                        <{FieldDescription}>Receive emails about new products, features, and more.</{FieldDescription}>
                    </{FieldContent}>
                </{Field}>
                <{Field}>
                    <{FieldLabel}>Privacy Settings</{FieldLabel}>
                    <{FieldDescription}>Manage your privacy preferences.</{FieldDescription}>
                    <{Field} orientation="horizontal">
                        <{Switch} id="switch-profile" defaultSelected />
                        <{FieldLabel} for="switch-profile">Make profile visible to others</{FieldLabel}>
                    </{Field}>
                    <{Field} orientation="horizontal">
                        <{Switch} id="switch-email" />
                        <{FieldLabel} for="switch-email">Show email on profile</{FieldLabel}>
                    </{Field}>
                </{Field}>
                <{Field} data-invalid orientation="horizontal">
                    <{FieldContent}>
                        <{FieldLabel} for="switch-invalid">Invalid Switch</{FieldLabel}>
                        <{FieldDescription}>This switch has validation errors.</{FieldDescription}>
                    </{FieldContent}>
                    <{Switch} id="switch-invalid" />
                </{Field}>
                <{Field} data-disabled orientation="horizontal">
                    <{FieldContent}>
                        <{FieldLabel} for="switch-disabled-field">Disabled Switch</{FieldLabel}>
                        <{FieldDescription}>This switch is currently disabled.</{FieldDescription}>
                    </{FieldContent}>
                    <{Switch} id="switch-disabled-field" isDisabled />
                </{Field}>
            </{FieldGroup}>
        </{Example}>
    """


def SliderFields():
    volume, set_volume = use_state([50])
    brightness, set_brightness = use_state([75])
    temperature, set_temperature = use_state([0.3, 0.7])
    price_range, set_price_range = use_state([25, 75])
    color_balance, set_color_balance = use_state([10, 20, 70])

    return t"""
        <{Example} title="Slider Fields">
            <{FieldGroup}>
                <{Field}>
                    <{FieldLabel} for="slider-volume">Volume</{FieldLabel}>
                    <{Slider} id="slider-volume" value={volume} onChange={set_volume} maxValue={100} step={1} />
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="slider-brightness">Screen Brightness</{FieldLabel}>
                    <{Slider} id="slider-brightness" value={brightness} onChange={set_brightness} maxValue={100} step={5} />
                    <{FieldDescription}>Current brightness: {brightness[0]}%</{FieldDescription}>
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="slider-quality">Video Quality</{FieldLabel}>
                    <{FieldDescription}>Higher quality uses more bandwidth.</{FieldDescription}>
                    <{Slider} id="slider-quality" defaultValue={[720]} maxValue={1080} minValue={360} step={360} />
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="slider-temperature">Temperature Range</{FieldLabel}>
                    <{Slider}
                        id="slider-temperature"
                        value={temperature}
                        onChange={set_temperature}
                        minValue={0}
                        maxValue={1}
                        step={0.1}
                    />
                    <{FieldDescription}>
                        Range: {temperature[0].toFixed(1)} - {temperature[1].toFixed(1)}
                    </{FieldDescription}>
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="slider-price-range">Price Range</{FieldLabel}>
                    <{Slider}
                        id="slider-price-range"
                        value={price_range}
                        onChange={set_price_range}
                        maxValue={100}
                        step={5}
                    />
                    <{FieldDescription}>${price_range[0]} - ${price_range[1]}</{FieldDescription}>
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="slider-color-balance">Color Balance</{FieldLabel}>
                    <{Slider}
                        id="slider-color-balance"
                        value={color_balance}
                        onChange={set_color_balance}
                        maxValue={100}
                        step={10}
                    />
                    <{FieldDescription}>
                        Red: {color_balance[0]}%, Green: {color_balance[1]}%, Blue:{" "}
                        {color_balance[2]}%
                    </{FieldDescription}>
                </{Field}>
                <{Field} data-invalid>
                    <{FieldLabel} for="slider-invalid">Invalid Slider</{FieldLabel}>
                    <{Slider} id="slider-invalid" defaultValue={[30]} maxValue={100} aria-invalid />
                    <{FieldDescription}>This slider has validation errors.</{FieldDescription}>
                </{Field}>
                <{Field} data-disabled>
                    <{FieldLabel} for="slider-disabled-field">Disabled Slider</{FieldLabel}>
                    <{Slider} id="slider-disabled-field" defaultValue={[50]} maxValue={100} isDisabled />
                    <{FieldDescription}>This slider is currently disabled.</{FieldDescription}>
                </{Field}>
            </{FieldGroup}>
        </{Example}>
    """


def InputOTPFields():
    value, set_value = use_state("")
    pin_value, set_pin_value = use_state("")

    return t"""
        <{Example} title="OTP Input Fields">
            <{FieldGroup}>
                <{Field}>
                    <{FieldLabel} for="otp-basic">Verification Code</{FieldLabel}>
                    <{InputOTP} id="otp-basic" maxLength={6}>
                        <{InputOTPGroup}>
                            <{InputOTPSlot} index={0} />
                            <{InputOTPSlot} index={1} />
                            <{InputOTPSlot} index={2} />
                            <{InputOTPSlot} index={3} />
                            <{InputOTPSlot} index={4} />
                            <{InputOTPSlot} index={5} />
                        </{InputOTPGroup}>
                    </{InputOTP}>
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="otp-with-desc">Enter OTP</{FieldLabel}>
                    <{InputOTP} id="otp-with-desc" maxLength={6} value={value} onChange={set_value}>
                        <{InputOTPGroup}>
                            <{InputOTPSlot} index={0} />
                            <{InputOTPSlot} index={1} />
                            <{InputOTPSlot} index={2} />
                            <{InputOTPSlot} index={3} />
                            <{InputOTPSlot} index={4} />
                            <{InputOTPSlot} index={5} />
                        </{InputOTPGroup}>
                    </{InputOTP}>
                    <{FieldDescription}>Enter the 6-digit code sent to your email.</{FieldDescription}>
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="otp-separator">Two-Factor Authentication</{FieldLabel}>
                    <{InputOTP} id="otp-separator" maxLength={6}>
                        <{InputOTPGroup}>
                            <{InputOTPSlot} index={0} />
                            <{InputOTPSlot} index={1} />
                            <{InputOTPSlot} index={2} />
                        </{InputOTPGroup}>
                        <{InputOTPSeparator} />
                        <{InputOTPGroup}>
                            <{InputOTPSlot} index={3} />
                            <{InputOTPSlot} index={4} />
                            <{InputOTPSlot} index={5} />
                        </{InputOTPGroup}>
                    </{InputOTP}>
                    <{FieldDescription}>Enter the code from your authenticator app.</{FieldDescription}>
                </{Field}>
                <{Field}>
                    <{FieldLabel} for="otp-pin">PIN Code</{FieldLabel}>
                    <{InputOTP}
                        id="otp-pin"
                        maxLength={4}
                        pattern={REGEXP_ONLY_DIGITS}
                        value={pin_value}
                        onChange={set_pin_value}
                    >
                        <{InputOTPGroup}>
                            <{InputOTPSlot} index={0} />
                            <{InputOTPSlot} index={1} />
                            <{InputOTPSlot} index={2} />
                            <{InputOTPSlot} index={3} />
                        </{InputOTPGroup}>
                    </{InputOTP}>
                    <{FieldDescription}>Enter your 4-digit PIN (numbers only).</{FieldDescription}>
                </{Field}>
                <{Field} data-invalid>
                    <{FieldLabel} for="otp-invalid">Invalid OTP</{FieldLabel}>
                    <{InputOTP} id="otp-invalid" maxLength={6}>
                        <{InputOTPGroup}>
                            <{InputOTPSlot} index={0} aria-invalid />
                            <{InputOTPSlot} index={1} aria-invalid />
                            <{InputOTPSlot} index={2} aria-invalid />
                            <{InputOTPSlot} index={3} aria-invalid />
                            <{InputOTPSlot} index={4} aria-invalid />
                            <{InputOTPSlot} index={5} aria-invalid />
                        </{InputOTPGroup}>
                    </{InputOTP}>
                    <{FieldDescription}>This OTP field contains validation errors.</{FieldDescription}>
                </{Field}>
                <{Field} data-disabled>
                    <{FieldLabel} for="otp-disabled-field">Disabled OTP</{FieldLabel}>
                    <{InputOTP} id="otp-disabled-field" maxLength={6} disabled>
                        <{InputOTPGroup}>
                            <{InputOTPSlot} index={0} />
                            <{InputOTPSlot} index={1} />
                            <{InputOTPSlot} index={2} />
                            <{InputOTPSlot} index={3} />
                            <{InputOTPSlot} index={4} />
                            <{InputOTPSlot} index={5} />
                        </{InputOTPGroup}>
                    </{InputOTP}>
                    <{FieldDescription}>This OTP field is currently disabled.</{FieldDescription}>
                </{Field}>
            </{FieldGroup}>
        </{Example}>
    """


def HorizontalFields():
    basic_items = [
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Orange", "value": "orange"},
    ]

    return t"""
        <{Example} title="Horizontal Fields">
            <{FieldGroup} class="**:data-[slot=field-content]:min-w-48">
                <{Field} orientation="horizontal">
                    <{FieldContent}>
                        <{FieldLabel} for="horizontal-input">Username</{FieldLabel}>
                        <{FieldDescription}>Enter your preferred username.</{FieldDescription}>
                    </{FieldContent}>
                    <{Input} id="horizontal-input" placeholder="johndoe" />
                </{Field}>
                <{Field} orientation="horizontal">
                    <{FieldContent}>
                        <{FieldLabel} for="horizontal-textarea">Bio</{FieldLabel}>
                        <{FieldDescription}>Write a short description about yourself.</{FieldDescription}>
                    </{FieldContent}>
                    <{Textarea} id="horizontal-textarea" placeholder="Tell us about yourself..." />
                </{Field}>
                <{Field} orientation="horizontal">
                    <{FieldContent}>
                        <{FieldLabel} for="horizontal-switch">Email Notifications</{FieldLabel}>
                        <{FieldDescription}>Receive email updates about your account.</{FieldDescription}>
                    </{FieldContent}>
                    <{Switch} id="horizontal-switch" />
                </{Field}>
                <{Field} orientation="horizontal">
                    <{FieldContent}>
                        <{FieldLabel} for="horizontal-select">Favorite Fruit</{FieldLabel}>
                        <{FieldDescription}>Choose your favorite fruit.</{FieldDescription}>
                    </{FieldContent}>
                    <{Select} placeholder="Select a fruit">
                        <{SelectTrigger} id="horizontal-select">
                            <{SelectValue} />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                {[t'''
                                    <{SelectItem}
                                        key={item["value"]}
                                        id={item["value"]}
                                    >
                                        {item["label"]}
                                    </{SelectItem}>
                                ''' for item in basic_items]}
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                </{Field}>
                <{Field} orientation="horizontal">
                    <{FieldContent}>
                        <{FieldLabel} for="horizontal-native-select">Country</{FieldLabel}>
                        <{FieldDescription}>Select your country.</{FieldDescription}>
                    </{FieldContent}>
                    <{NativeSelect} id="horizontal-native-select">
                        <{NativeSelectOption} value="">Select a country</{NativeSelectOption}>
                        <{NativeSelectOption} value="us">United States</{NativeSelectOption}>
                        <{NativeSelectOption} value="uk">United Kingdom</{NativeSelectOption}>
                        <{NativeSelectOption} value="ca">Canada</{NativeSelectOption}>
                    </{NativeSelect}>
                </{Field}>
                <{Field} orientation="horizontal">
                    <{FieldContent}>
                        <{FieldLabel} for="horizontal-slider">Volume</{FieldLabel}>
                        <{FieldDescription}>Adjust the volume level.</{FieldDescription}>
                    </{FieldContent}>
                    <{Slider} id="horizontal-slider" defaultValue={[50]} maxValue={100} />
                </{Field}>
            </{FieldGroup}>
        </{Example}>
    """
