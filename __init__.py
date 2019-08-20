# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "ToFlat",
    "author": "NorthForge",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "View3D",
    "description": "Allows you to switch the view to see the silhouette of the model, and switch the view back Usage: Object->ToFlat",
    "warning": "",
    "category": "3DView",
}

import bpy

from . toFlat import ToFlat
from . toFlat import menu_func

def register():
    bpy.utils.register_class(ToFlat)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(ToFlat)
    bpy.types.VIEW3D_MT_object.remove(menu_func)