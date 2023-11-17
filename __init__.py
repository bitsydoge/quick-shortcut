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

from . import (
	area_shortcut
)

bl_info = {
	"name": "quick-shortcut",
	"description": "",
	"author": "bitsydoge",
	"version": (1, 0, 0),
	"blender": (3, 6, 0),
	"support": "COMMUNITY",
	"category": "Utility"
}


####################################################
# Register
####################################################

def register():
	area_shortcut.register()


def unregister():
	area_shortcut.unregister()