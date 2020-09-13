bl_info = {
    "name": "Eevee Config",
    "author": "Rithvik Kadiresan",
    "version": (1, 0),
    "blender": (2, 90, 0),
    "location": "PROPERTIES > SCENE > Eevee Config",
    "description": "Adds a new Mesh Object",
    "warning": "Auto Baking lighting can cuase performance to slow down.",
    "doc_url": "",
    "category": "Scene Setup",
}

import bpy

def main(context):
    bpy.context.scene.render.engine = 'BLENDER_EEVEE'
    bpy.context.scene.eevee.use_gtao = True
    bpy.context.scene.eevee.use_bloom = True
    bpy.context.scene.eevee.use_ssr = True
    bpy.context.scene.eevee.use_motion_blur = True
    bpy.ops.object.lightprobe_add(type='GRID')
    bpy.ops.transform.resize(value=(5, 5, 5), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.collection.create()
    bpy.ops.object.move_to_collection(collection_index=0, is_new=True, new_collection_name="Eevee Config Light Probe")    
    bpy.context.scene.eevee.gi_auto_bake = True
    bpy.context.scene.eevee.use_ssr_refraction = True
    bpy.context.space_data.shading.type = 'RENDERED'


class EeveeConfig(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "scene.eevee_config"
    bl_label = "Eevee Config"



    def execute(self, context):
        main(context)
        return {'FINISHED'}



##Panel code below



class EeveeConfigPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Eevee Config"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene


        # Big render button
        layout.label(text="Enhance Realtime:")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("scene.eevee_config")


addon_keymaps = []

def register():
    bpy.utils.register_class(EeveeConfigPanel)
    bpy.utils.register_class(EeveeConfig)
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new("scene.eevee_config", type= 'E', value= 'PRESS', ctrl= True)
        addon_keymaps.append((km, kmi))


def unregister():
    for km,kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()    
    
    bpy.utils.unregister_class(EeveeConfigPanel)
    bpy.utils.unregister_class(EeveeConfig)


if __name__ == "__main__":
    register()



# test call
#bpy.ops.scene.eevee_config()
