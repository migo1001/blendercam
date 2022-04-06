
import unittest
import bpy

info_panel = None

class TestInfoPanel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        for panel in bpy.types.Panel.__subclasses__():
            if panel.__name__ == "CAM_INFO_Panel":
                cls.info_panel = panel()
                continue

    def test_addon_enabled(self):
        info_panel = None
        self.assertIsNotNone(self.info_panel)
        self.assertEqual("CAM info & warnings", self.info_panel.bl_label)

    def test_warnings(self):
        self.assertEqual("CAM info & warnings", self.info_panel.draw_active_op_warnings())

    def test_opencamlib(self):
        self.assertEqual("Opencamlib vxxxx installed", TestInfoPanel.info_panel.draw_opencamlib_version())



    def test_hourly_rate(self):
        self.assertIsNotNone(bpy.context.scene.cam_machine.hourly_rate)
        bpy.context.scene.cam_machine.hourly_rate = 200.0
        self.assertEqual(bpy.context.scene.cam_machine.hourly_rate, 200.0)

suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestInfoPanel)
unittest.TextTestRunner().run(suite)
