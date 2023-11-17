import bpy


class NODE_OT_switch_editors_to_compositor(bpy.types.Operator):
	"""Switch to the Comppositor Editor"""

	bl_idname = "wm.switch_editor_to_compositor"
	bl_label = "Switch to Compositor Editor"
	bl_options = {"REGISTER", "UNDO"}

	def execute(self, context):
		bpy.ops.wm.context_set_enum(
			data_path="area.ui_type", value="CompositorNodeTree"
		)
		return {"FINISHED"}


class NODE_OT_switch_editors_to_geometry(bpy.types.Operator):
	"""Switch to the Geometry Node Editor"""

	bl_idname = "wm.switch_editor_to_geometry"
	bl_label = "Switch to Geometry Node Editor"
	bl_options = {"REGISTER", "UNDO"}

	def execute(self, context):
		bpy.ops.wm.context_set_enum(data_path="area.ui_type", value="GeometryNodeTree")
		return {"FINISHED"}


class NODE_OT_switch_editors_to_shadereditor(bpy.types.Operator):
	"""Switch to the Shader Editor"""

	bl_idname = "wm.switch_editor_to_shadereditor"
	bl_label = "Switch to Shader Editor"
	bl_options = {"REGISTER", "UNDO"}

	def execute(self, context):
		bpy.ops.wm.context_set_enum(data_path="area.ui_type", value="ShaderNodeTree")
		return {"FINISHED"}


class NODE_OT_switch_editors_in_compositor(bpy.types.Operator):
	"""Compositor Editor"""

	bl_idname = "wm.switch_editor_in_compositor"
	bl_label = "You are in Compositor Editor"
	bl_options = {"REGISTER", "UNDO"}

	def execute(self, context):
		return {"FINISHED"}


class NODE_OT_switch_editors_in_geometry(bpy.types.Operator):
	"""Geometry Node Editor"""

	bl_idname = "wm.switch_editor_in_geometry"
	bl_label = "You are in Geometry Node Editor"
	bl_options = {"REGISTER", "UNDO"}

	def execute(self, context):
		return {"FINISHED"}


class NODE_OT_switch_editors_in_shadereditor(bpy.types.Operator):
	"""Shader Editor"""

	bl_idname = "wm.switch_editor_in_shadereditor"
	bl_label = "You are in Shader Editor"
	bl_options = {"REGISTER", "UNDO"}

	def execute(self, context):
		return {"FINISHED"}
