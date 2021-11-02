# plover-comment

Plover plugin to add comment/meta-information to the outline definition.

## Usage

In order to use this plugin in [Plover](https://github.com/openstenoproject/plover) you need to
create a dictionary entry of the form:

``` json
{
    "example_stroke": "{:COMMENT:some comment text here}"
}
```

`COMMENT` can be replaced with `CMT` for short.

They're still subject to the rules of JSON and Plover atom, so any `{` and `}` inside the comment
must be escaped.

Alternatively the command form `{PLOVER:COMMENT:some comment text here}` can also be used.

In some new Plover version `{:comment:some comment text here}` would also work.
