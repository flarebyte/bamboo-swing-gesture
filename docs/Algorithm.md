# Useful Algorithms

## Coordinates

### Cartesian coordinates

* 2 dimensions (x, y)
* 3 dimensions (x, y, z)

[Cartesian coordinate system](https://en.wikipedia.org/wiki/Cartesian_coordinate_system)

### Polar coordinates

* 2 dimensions (r, theta)

Conversion to Cartesian:

```
x = r * cos(theta)
y = r * sin(theta)
```
or from Cartesian:

```
r = sqrt(x**2 + y**2)
theta = atan2(y, x)

```

[Polar coordinate system](https://en.wikipedia.org/wiki/Polar_coordinate_system)

## Distance between two points

### Cartesian

For points (x1, y1) and (x2, y2)

```distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)```

For point (x1, y1, z1) and (x2, y2, z2)

```distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)+ (z2 - z1)**2)```


## Rotation

### Cartesian

For point (x, y) and angle theta

```
x2 = x * cos(theta) - y * sin(theta)
y2 = x * sin(theta) + y * cos(theta)
```

## Reflection

For point (x, y) and angle theta

```
x2 = x*cos(2*theta) + y*sin(2*theta)
y2 = x*sin(2*theta) - y*cos(2*theta)
```

## Circle

### Polar

Center as (r0, theta0) and radius a

``` r**2 -2*r*r0*cos(theta-theta0) + r0**2 = a**2 ```

## Bezier



## Shadow

