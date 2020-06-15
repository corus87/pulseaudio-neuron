# Pulseaudio
Pulseaudio neuron for Kalliope

## Synopsis
Volume and microphone controll for pulseaudio

## Installation
```bash
kalliope install --git-url https://github.com/corus87/pulseaudio-neuron
```

## Options

| Parameter     | Required | Choices                          |
|---------------|----------|----------------------------------|
| volume        | no       | 1-150                            |
| input_device  | yes      | device ID for your input device  |
| output_device | yes      | device ID for your output device |



## Return values

| Name           | Description                                  |
|----------------|----------------------------------------------|
| volume         | Returns the volume                           |

## Notes
You can use either input_device or output_device. If you don't use volume, you will get the current volume of the device you set. 

To get the index for the input_device, run ```pacmd list-sources | grep -e 'name:' -e 'index:```
For the output_device, run  ```pacmd list-sinks | grep -e 'name:' -e 'index:'```


## Synapses example
```
  - name: "set-output-volume"
    signals:
      - order: "Set output volume to {{ volume }}"
    neurons: 
      - pulseaudio:
          volume: "{{ volume }}"
          output_device: 0
          say_template: "I have set the output volume to {{ volume }}"


  - name: "set-mic-volume"
    signals:
      - order: "Set microphone volume to {{ volume }}"
    neurons: 
      - pulseaudio:
          volume: "{{ volume }}"
          output_device: 0
          say_template: "I have set the microphone volume to {{ volume }}"


  - name: "current-volume"
    signals:
      - order: "what is the current speaker volume"
    neurons: 
      - pulseaudio:
          output_device: 0
          say_template: "The current volume is {{ volume }}"

```

