# Spike

## Summary

* Dependencies are downloaded though a script. I tend to prefer a declarative approach such as package.json in node.js, but why not.
* Creating an image requires very simple code.
* Julia supports Rational numbers by default.
* Performances: 16 seconds for creating an image seems a bit slow but worth checking what are the performances with other languages.


## Performances:

On a Mac: 1.1 GHz Intel Core m3.
julia version 1.3.0

``` rand(width,height) ```

| Resolution | Time       |
| ---------- | ---------- |
|1024*768    | 11 seconds |
|4000*3000   | 11 seconds |

```
details = rand(width,height)
save("../temp/gray.png", colorview(Gray, details))
```

| Resolution | Time       |
| ---------- | ---------- |
|1024*768    | 16 seconds |
|4000*3000   | 17 seconds |



