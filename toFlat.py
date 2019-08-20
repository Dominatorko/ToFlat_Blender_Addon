import bpy

class ToFlat(bpy.types.Operator):

    toFlatLight = 'FLAT'
    toFlatColorType = 'SINGLE'

    bl_idname = "shading.light"
    bl_label = "ToFlat"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        global toFlatLight
        global toFlatColorType
        my_areas = bpy.context.workspace.screens[0].areas
        for area in my_areas:
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    if space.shading.light != 'FLAT':
                        toFlatLight = space.shading.light
                        toFlatColorType = space.shading.color_type
                        space.shading.light = 'FLAT'
                        space.shading.color_type = 'SINGLE'
                        space.shading.single_color = (0, 0, 0)
                        return {'FINISHED'}
                    else:
                        space.shading.light = toFlatLight
                        space.shading.color_type = toFlatColorType
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(ToFlat.bl_idname)