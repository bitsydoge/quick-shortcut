import bpy

from .file import FILE_OT_switch_editors_to_filebrowser, FILE_OT_switch_editors_to_asset
from .image import IMAGE_OT_switch_editors_to_uv, IMAGE_OT_switch_editors_to_image
from .node import NODE_OT_switch_editors_to_compositor, NODE_OT_switch_editors_to_geometry, \
	NODE_OT_switch_editors_to_shadereditor, NODE_OT_switch_editors_in_compositor, NODE_OT_switch_editors_in_geometry, \
	NODE_OT_switch_editors_in_shadereditor


def node_shortcuts(self, context):
	snode = context.space_data
	layout: bpy.types.UILayout = self.layout
	geonodeicon = "NODETREE" if (3, 3, 0) > bpy.app.version else "GEOMETRY_NODES"

	if snode.tree_type == "ShaderNodeTree":
		row = layout.row(align=True)
		row.operator(
			"wm.switch_editor_in_shadereditor",
			text="Mat",
			icon="NODE_MATERIAL",
			depress=True,
		)
		row.operator("wm.switch_editor_to_geometry", text="Geo", icon=geonodeicon)
		row.operator(
			"wm.switch_editor_to_compositor", text="Comp", icon="NODE_COMPOSITING"
		)

	elif snode.tree_type == "CompositorNodeTree":
		row = layout.row(align=True)
		row.operator(
			"wm.switch_editor_to_shadereditor", text="Mat", icon="NODE_MATERIAL"
		)
		row.operator("wm.switch_editor_to_geometry", text="Geo", icon=geonodeicon)
		row.operator(
			"wm.switch_editor_in_compositor",
			text="Comp",
			icon="NODE_COMPOSITING",
			depress=True,
		)

	elif snode.tree_type == "GeometryNodeTree":
		row = layout.row(align=True)
		row.operator(
			"wm.switch_editor_to_shadereditor", text="Mat", icon="NODE_MATERIAL"
		)
		row.operator(
			"wm.switch_editor_in_geometry", text="Geo", icon=geonodeicon, depress=True
		)
		row.operator(
			"wm.switch_editor_to_compositor", text="Comp", icon="NODE_COMPOSITING"
		)


def image_shortcuts(self, context):
	layout: bpy.types.UILayout = self.layout
	if context.space_data.mode != "UV":
		row = layout.row(align=True)
		row.operator("wm.switch_editor_to_uv", text="", icon="UV")
	else:
		row = layout.row(align=True)
		row.operator("wm.switch_editor_to_image", text="", icon="IMAGE")


def file_shortcuts(self, context):
	from bpy_extras.asset_utils import SpaceAssetInfo

	layout: bpy.types.UILayout = self.layout
	space_data = context.space_data

	if SpaceAssetInfo.is_asset_browser(space_data):
		row = layout.row(align=True)
		row.operator("wm.switch_editor_to_filebrowser", text="", icon="FILEBROWSER")
	else:
		row = layout.row(align=True)
		row.operator("wm.switch_editor_to_asset", text="", icon="ASSET_MANAGER")


classes = (
	NODE_OT_switch_editors_in_shadereditor,
	NODE_OT_switch_editors_in_geometry,
	NODE_OT_switch_editors_in_compositor,
	NODE_OT_switch_editors_to_shadereditor,
	NODE_OT_switch_editors_to_compositor,
	NODE_OT_switch_editors_to_geometry,
	IMAGE_OT_switch_editors_to_uv,
	IMAGE_OT_switch_editors_to_image,
	FILE_OT_switch_editors_to_asset,
	FILE_OT_switch_editors_to_filebrowser,
)


def register():
	from bpy.utils import register_class

	for c in classes:
		register_class(c)

	bpy.types.NODE_HT_header.prepend(node_shortcuts)
	bpy.types.IMAGE_HT_header.prepend(image_shortcuts)
	bpy.types.FILEBROWSER_HT_header.prepend(file_shortcuts)


def unregister():
	bpy.types.FILEBROWSER_HT_header.remove(file_shortcuts)
	bpy.types.IMAGE_HT_header.remove(image_shortcuts)
	bpy.types.NODE_HT_header.remove(node_shortcuts)

	from bpy.utils import unregister_class

	for c in reversed(classes):
		unregister_class(c)
