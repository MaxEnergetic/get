import time
import smbus
import signal_generator as sg


class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose=True):
        self.bus = smbus.SMBus(1)
        self.address = address
        self.wm = 0x00
        self.pds = 0x00
        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")
            return

        if not (0 <= number <= 4095):
            print("Число выходит за разрядность MCP4725 (12 бит)")
            return

        first_byte = self.wm | self.pds | (number >> 8)
        second_byte = number & 0xFF

        self.bus.write_byte_data(self.address, first_byte, second_byte)

        if self.verbose:
            print(
                f"Число: {number}, отправленные по I2C данные: "
                f"[0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]"
            )

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(
                f"Напряжение выходит за диапазон (0 - {self.dynamic_range:.2f} В)"
            )
            print("Устанавливаем 0 В")
            voltage = 0.0

        number = int(voltage / self.dynamic_range * 4095)
        self.set_number(number)


if __name__ == "__main__":

    frequency = 5              
    sampling_frequency = 50    
    dynamic_range = 3.3        
    t = 0.0

    try:
        dac = MCP4725(dynamic_range, 0x61, True)

        freq = 5  
        sampling_frequency = 50  
        t = 0.0

        while True:
            amp = sg.triangle_signal(freq, t)    
            voltage = amp * dac.dynamic_range
            dac.set_voltage(voltage)
            sg.wait_for_sampling_period(sampling_frequency)
            t += 1.0 / sampling_frequency

    finally:
        dac.deinit()
