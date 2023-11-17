import pytest
from television import Television

class TestTelevision:
    def setup_method(self):
        self.tv1 = Television()
        
    def teardown_method(self):
        del self.tv1

    def test_init(self):
        assert str(self.tv1) == "Power [False], Channel [0], Volume [0]"

    def test_power(self):
        self.tv1.power()
        assert str(self.tv1) == "Power [True], Channel [0], Volume [0]"

        self.tv1.power()
        assert str(self.tv1) == "Power [False], Channel [0], Volume [0]"

    def test_mute(self):
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute()
        assert str(self.tv1) == "Power [True], Channel [0], Volume [Muted]"

        self.tv1.mute()
        assert str(self.tv1) == "Power [True], Channel [0], Volume [0]"

        self.tv1.power()
        self.tv1.mute()
        assert str(self.tv1) == "Power [False], Channel [0], Volume [0]"

        self.tv1.power()
        assert str(self.tv1) == "Power [True], Channel [0], Volume [0]"

    def test_channel_up(self):
        self.tv1.channel_up()
        assert str(self.tv1) == "Power [False], Channel [0], Volume [0]"

        self.tv1.power()
        self.tv1.channel_up()
        assert str(self.tv1) == "Power [True], Channel [1], Volume [0]"

        for _ in range(Television.MAX_CHANNEL):
            self.tv1.channel_up()

        assert str(self.tv1) == "Power [True], Channel [0], Volume [0]"

    def test_channel_down(self):
        self.tv1.channel_down()
        assert str(self.tv1) == "Power [False], Channel [0], Volume [0]"

        self.tv1.power()
        self.tv1.channel_down()
        assert str(self.tv1) == "Power [True], Channel [2], Volume [0]"

        for _ in range(Television.MAX_CHANNEL):
            self.tv1.channel_down()

        assert str(self.tv1) == "Power [True], Channel [3], Volume [0]"

    def test_volume_up(self):
        self.tv1.volume_up()
        assert str(self.tv1) == "Power [False], Channel [0], Volume [0]"

        self.tv1.power()
        self.tv1.volume_up()
        assert str(self.tv1) == "Power [True], Channel [0], Volume [1]"

        for _ in range(Television.MAX_VOLUME):
            self.tv1.volume_up()

        assert str(self.tv1) == "Power [True], Channel [0], Volume [2]"

    def test_volume_down(self):
        self.tv1.volume_down()
        assert str(self.tv1) == "Power [False], Channel [0], Volume [0]"

        self.tv1.power()
        self.tv1.volume_up() 
        self.tv1.volume_down()
        assert str(self.tv1) == "Power [True], Channel [0], Volume [1]"

        for _ in range(Television.MIN_VOLUME):
            self.tv1.volume_down()

        assert str(self.tv1) == "Power [True], Channel [0], Volume [0]"
