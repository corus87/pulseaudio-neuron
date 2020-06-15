# -*- coding: iso-8859-1 -*-
from kalliope.core.NeuronModule import NeuronModule, MissingParameterException
from kalliope import Utils
import pulsectl
import re

class Pulseaudio(NeuronModule):
    def __init__(self, **kwargs):
        super(Pulseaudio, self).__init__(**kwargs)
        # the args from the neuron configuration
        self.volume = kwargs.get('volume', None)
        self.input_device = kwargs.get('input_device', None)
        self.output_device = kwargs.get('output_device', None)

        sink = None
        if self._is_parameters_ok():
            # pacmd list-sinks | grep -e 'name:' -e 'index:' get all outputs
            # pacmd list-sources | grep -e 'name:' -e 'index:' get all inputs
            # pacmd set-default-sink default_output

            pulse = pulsectl.Pulse()
            if self.input_device or self.input_device == 0:
              sink = pulse.source_list()[self.input_device]
            if self.output_device or self.output_device == 0:
              sink = pulse.sink_list()[self.output_device]
            if sink:
                if self.volume:
                    if self.hasNumbers(self.volume):
                        values = self.values()
                        volume = re.sub("[^0-9]", "", self.volume)
                        for k, p in values.items():
                            if int(volume) == k:
                                volume = p
                        if int(volume) > 1.5:
                            raise MissingParameterException("[PulseAudio] %s is out of range!" % volume)
                        pulse.volume_set_all_chans(sink, volume)

                current_volumes = str(sink.volume).split("volumes=[",1)[1] 
                current_vol = re.findall(r'\d+', current_volumes)
                self.say({"volume": current_vol[0]})
            else:
                raise MissingParameterException("[PulseAudio] No Input or Output device selected")
    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise

        .. raises:: MissingParameterException
        """

        return True

    def hasNumbers(self, inputString):
         return any(char.isdigit() for char in inputString)

    def values(self):
        return {0:0,
              1:0.01,
              2:0.02,
              3:0.03,
              4:0.04,
              5:0.05,
              6:0.06,
              7:0.07,
              8:0.08,
              9:0.09,
              10:0.1,
              11:0.11,
              12:0.12,
              13:0.13,
              14:0.14,
              15:0.15,
              16:0.16,
              17:0.17,
              18:0.18,
              19:0.19,
              20:0.2,
              21:0.21,
              22:0.22,
              23:0.23,
              24:0.24,
              25:0.25,
              26:0.26,
              27:0.27,
              28:0.28,
              29:0.29,
              30:0.3,
              31:0.31,
              32:0.32,
              33:0.33,
              34:0.34,
              35:0.35,
              36:0.36,
              37:0.37,
              38:0.38,
              39:0.39,
              40:0.4,
              41:0.41,
              42:0.2,
              43:0.43,
              44:0.44,
              45:0.45,
              46:0.46,
              47:0.47,
              48:0.48,
              49:0.49,
              50:0.5,
              51:0.51,
              52:0.52,
              53:0.53,
              54:0.54,
              55:0.55,
              56:0.56,
              57:0.57,
              58:0.58,
              59:0.59,
              60:0.6,
              61:0.61,
              62:0.62,
              63:0.63,
              64:0.64,
              65:0.65,
              66:0.66,
              67:0.67,
              68:0.68,
              69:0.69,
              70:0.7,
              71:0.71,
              72:0.72,
              73:0.73,
              74:0.74,
              75:0.75,
              76:0.76,
              77:0.77,
              78:0.78,
              79:0.79,
              80:0.8,
              81:0.81,
              82:0.82,
              83:0.83,
              84:0.84,
              85:0.85,
              86:0.86,
              87:0.87,
              88:0.88,
              89:0.89,
              90:0.9,
              91:0.91,
              92:0.92,
              93:0.93,
              94:0.94,
              95:0.95,
              96:0.96,
              97:0.97,
              98:0.98,
              99:0.99,
              100:1,
              101:1.01,
              102:1.02,
              103:1.03,
              104:1.04,
              105:1.05,
              106:1.06,
              107:1.07,
              108:1.08,
              109:1.09,
              110:1.1,
              111:1.11,
              112:1.12,
              113:1.13,
              114:1.14,
              115:1.15,
              116:1.16,
              117:1.17,
              118:1.18,
              119:1.19,
              120:1.2,
              121:1.21,
              122:1.22,
              123:1.23,
              124:1.24,
              125:1.25,
              126:1.26,
              127:1.27,
              128:1.28,
              129:1.29,
              130:1.3,
              131:1.31,
              132:1.32,
              133:1.33,
              134:1.34,
              135:1.35,
              136:1.36,
              137:1.37,
              138:1.38,
              139:1.39,
              140:1.4,
              141:1.41,
              142:1.42,
              143:1.43,
              144:1.44,
              145:1.45,
              146:1.46,
              147:1.47,
              148:1.48,
              149:1.49,
              150:1.5
              }