# List all the vertices in a profile list
# This is just a simplified version of:
#   http://pacific.mpi-cbg.de/wiki/index.php/TrakEM2_Scripting#Measure_the_minimal_distance_from_each_ball_to_a_surface_defined_by_a_profile_list

from ini.trakem2.display import Display, Profile
from java.util import HashSet

def run():
  front = Display.getFront()
  if front is None:
    IJ.error("No displays open!")
    return
  sel = front.getSelection().getSelected(Profile)
  if sel.isEmpty():
    IJ.error("No profile was selected")
    return
  if sel.size() > 1:
    IJ.error("More than one object is selected")
    return
  profile = sel.get(0)
  if profile.getClass() != Profile:
    IJ.error("The selected object isn't a Profile - it's of class '"+str(profile.getClass()))
    return
  profile_list = profile.project.findProjectThing(profile).getParent()
  print "Got profile_list", profile_list, "of class", profile_list.getClass()
  # If you need the mesh structure, you can use the list of triangles:
  triangles = Profile.generateTriangles(profile_list, 1)
  # If you just want the vertices, you can collapse them into a
  # HashSet to remove duplicates:
  verts = HashSet(triangles)
  print "Got verts:", verts

run()
