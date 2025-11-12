from graphics.rectangle import area as rect_area, perimeter as rect_peri
from graphics.circle import area as circ_area
from graphics.graphics_3D.cuboid import perimeter as cuboid_peri

print("Rectangle area:", rect_area(10, 5))
print("Rectangle perimeter:", rect_peri(10, 5))
print("Circle area:", circ_area(7))
print("Cuboid perimeter:", cuboid_peri(3, 4, 5))
