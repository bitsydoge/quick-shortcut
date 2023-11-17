import bpy


class FILE_OT_switch_editors_to_filebrowser(bpy.types.Operator):
	"""Switch to the Filebrowser"""

	bl_idname = "wm.switch_editor_to_filebrowser"
	bl_label = "Switch to UV Editor"
	bl_options = {"REGISTER", "UNDO"}

	def execute(self, context):
		bpy.ops.wm.context_set_enum(data_path="area.ui_type", value="FILES")
		return {"FINISHED"}


class FILE_OT_switch_editors_to_asset(bpy.types.Operator):
	"""Switch to the Asset Browser"""

	bl_idname = "wm.switch_editor_to_asset"
	bl_label = "Switch to Image Editor"
	bl_options = {"REGISTER", "UNDO"}

	def execute(self, context):
		bpy.ops.wm.context_set_enum(data_path="area.ui_type", value="ASSETS")
		return {"FINISHED"}
