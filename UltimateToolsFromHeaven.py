bl_info = {
    "name": "ToFlat",
    "author": "NorthForge",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "View3D",
    "description": "ToFlat: Allows you to switch the view to see the silhouette of the model, and switch the view back Usage: Object->ADDON_ToFlat",
    "warning": "",
    "category": "3DView",
}

import bpy

class ToFlat(bpy.types.Operator):
    
    mLight =''
    mColorType = ''
   
    bl_idname = "shading.light"
    bl_label = "ADDON_ToFlat"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        global mLight
        global mColorType
        my_areas = bpy.context.workspace.screens[0].areas
        for area in my_areas:
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    if space.shading.light != 'FLAT':
                        mLight = space.shading.light
                        mColorType = space.shading.color_type
                        print(mLight)
                        print(mColorType)
                        space.shading.light = 'FLAT'
                        space.shading.color_type = 'SINGLE'
                        space.shading.single_color = (0,0,0)
                    else:
                        space.shading.light = mLight
                        space.shading.color_type = mColorType
        return {'FINISHED'}     
    
def menu_func(self, context):
    self.layout.operator(ToFlat.bl_idname)     

def register():
    bpy.utils.register_class(ToFlat)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(ToFlat)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
