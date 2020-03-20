
from __future__ import with_statement

import sys
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import *
from _Framework.ButtonElement import ButtonElement
from _Framework.TransportComponent import TransportComponent
from _Framework.DeviceComponent import DeviceComponent
from _Framework.EncoderElement import EncoderElement
from _Framework.SessionZoomingComponent import SessionZoomingComponent

from _Framework.ChannelStripComponent import ChannelStripComponent
from _APC.DetailViewCntrlComponent import DetailViewCntrlComponent

from DeviceNavComponent import DeviceNavComponent

from _Framework.SliderElement import SliderElement # Class representing a slider on the controller
from consts import *
mixer = None


class skym(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        self._device_selection_follows_track_selection = True
        with self.component_guard():
            self._suppress_send_midi = True
            self._suppress_session_highlight = True
            self._control_is_with_automap = False
            is_momentary = True
            self._suggested_input_port = 'iPhone'
            self._suggested_output_port = 'iPhone'
            self.log("BEFORE mixer")
            self._setup_mixer_control()
            self._setup_device_control()


    def log(self, message):
        sys.stderr.write("LOG: " + message.encode("utf-8"))


    def _setup_mixer_control(self):
        """TRANSPORT CONTROLS"""
        stop_button = ButtonElement(False, MIDI_CC_TYPE, 0, STOP_BUTTON)
        play_button = ButtonElement(False, MIDI_CC_TYPE, 0, PLAY_BUTTON)
        record_button = ButtonElement(False,MIDI_CC_TYPE,0,RECORD_BUTTON)
        transport = TransportComponent()
        transport.set_stop_button(stop_button)
        transport.set_play_button(play_button)
        transport.set_overdub_button(record_button)
        transport.set_overdub_button(record_button)
        transport.set_seek_buttons(ButtonElement(False,MIDI_CC_TYPE,0,SEEK_LEFT),ButtonElement(False,MIDI_CC_TYPE,0,SEEK_RIGHT))

    def _setup_device_control(self):
        is_momentary = True
        self._device = DeviceComponent()
        self._channelstrip = ChannelStripComponent()
        self._device.name = 'Device_Component'

        device_param_controls = []
        for index in range(8):
            device_param_controls.append(SliderElement(MIDI_CC_TYPE, CHANNEL, MACRO_CONTROLS[index]))
        self._device.set_parameter_controls(device_param_controls)
        # self._device.set_on_off_button(ButtonElement(True, MIDI_CC_TYPE, CHANNEL, DEVICE_ON))
        self._device.set_lock_button(ButtonElement(True, MIDI_CC_TYPE, CHANNEL, DEVICE_LOCK))
        # self._device.set_bank_down_value(ButtonElement(True, MIDI_CC_TYPE, CHANNEL, DEVICE_LOCK))
        # self._device.set_bank_up_value(ButtonElement(True, MIDI_CC_TYPE, CHANNEL, DEVICE_ON))
        up_bank_button = ButtonElement(True, MIDI_CC_TYPE, CHANNEL, DEVICE_ON)
        down_bank_button = ButtonElement(True, MIDI_CC_TYPE, CHANNEL, DEVICE_LOCK)
        # self._device.set_bank_buttons(down_bank_button, up_bank_button)
        self.set_device_component(self._device)
        self._device_nav = DeviceNavComponent()
        self._device_nav.set_device_nav_buttons(ButtonElement(True, MIDI_CC_TYPE, CHANNEL, PREVIOUS_DEVICE),ButtonElement(True, MIDI_CC_TYPE, CHANNEL, NEXT_DEVICE))
        self._device.set_bank_prev_button(down_bank_button)
        self._device.set_bank_next_button(up_bank_button)


    def disconnect(self):
        """clean things up on disconnect"""
        ControlSurface.disconnect(self)
        return None
