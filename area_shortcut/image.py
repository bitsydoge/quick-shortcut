import bpy


class IMAGE_OT_switch_editors_to_uv(bpy.types.Operator):
	"""Switch to the UV Editor"""

	bl_idname = "wm.switch_editor_to_uv"
	bl_label = "Switch to UV Editor"
	bl_options = {"REGISTER", "UNDO"}

	def execute(self, context):
		bpy.ops.wm.context_set_enum(data_path="area.ui_type", value="UV")
		return {"FINISHED"}


class IMAGE_OT_switch_editors_to_image(bpy.types.Operator):
	"""Switch to the Image Editor"""

	bl_idname = "wm.switch_editor_to_image"
	bl_label = "Switch to Image Editor"
	bl_options = {"REGISTER", "UNDO"}

	def execute(self, context):
		bpy.ops.wm.context_set_enum(data_path="area.ui_type", value="IMAGE_EDITOR")
		return {"FINISHED"}
