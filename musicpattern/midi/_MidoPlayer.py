

class MidoPlayer:

    def __init__(self, device_index=None):
        self.device_index = device_index
        self.output = None

    def play(self, midifile):
        self.setup()

        for msg in midifile.play():
            #print(msg)
            self.output.send(msg)

    def setup(self):
        import mido
        if not self.output:
            ports = mido.get_output_names()

            if self.device_index is None:
                for i, p in enumerate(ports):
                    print("[%s] %s" % (i, p))
                self.device_index = int(input("select index: "))

            self.output = mido.open_output(ports[self.device_index])

        return self.output