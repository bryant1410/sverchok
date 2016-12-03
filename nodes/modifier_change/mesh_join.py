# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy

from sverchok.node_tree import SverchCustomTreeNode
from sverchok.utils.sv_mesh_utils import mesh_join


class SvMeshJoinNode(bpy.types.Node, SverchCustomTreeNode):
    '''MeshJoin, join many mesh into on mesh object'''
    bl_idname = 'SvMeshJoinNode'
    bl_label = 'Mesh Join'
    bl_icon = 'OUTLINER_OB_EMPTY'

    def sv_init(self, context):
        self.inputs.new('VerticesSocket', 'Vertices', 'Vertices')
        self.inputs.new('StringsSocket', 'PolyEdge', 'PolyEdge')

        self.outputs.new('VerticesSocket', 'Vertices', 'Vertices')
        self.outputs.new('StringsSocket', 'PolyEdge', 'PolyEdge')

    def process(self):
        Vertices, PolyEdge = self.inputs
        Vertices_out, PolyEdge_out = self.outputs

        if Vertices.is_linked
            verts = Vertices.sv_get()

            poly_edge = PolyEdge.sv_get(default=[[]])
            verts_out, dummy, poly_edge_out = mesh_join(verts, [], poly_edge)

            if Vertices_out.is_linked:
                Vertices_out.sv_set([verts_out])

            if PolyEdge_out.is_linked:
                PolyEdge_out.sv_set([poly_edge_out])


def register():
    bpy.utils.register_class(SvMeshJoinNode)


def unregister():
    bpy.utils.unregister_class(SvMeshJoinNode)
