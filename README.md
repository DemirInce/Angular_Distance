# Angular_Distance

Measures the angular distance between any two points on a 360-degree by 180-degree image from a 360 camera. An image with a 2:1 aspect ratio is required.

Usage: measure.py [-h] [-i IMAGE] [-f FONT SIZE]

options:  
	-h, --help               -> show help menu  
	-i IMAGE, --image IMAGE  -> path to image, defaults to 'Test.jpg'  
 	-f FONT SIZE, --font_size FONT SIZE -> adjusts font size, defaults to 14

Click on two points to measure the distance. 

"Backspace" to delete the last measurement. 

"C" to clear all measurements.

Note: The distortions are a result of the equirectangular projection onto a flat surface. During calculation the image is projected to the inside of a sphere and the segment of the great circle in between the two points is measured. The straight lines draw are simply for reference, the number displayed is the true measurement.
