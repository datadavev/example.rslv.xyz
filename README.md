# echo.rslv.xyz

A reflector site, returning the request as JSON, excluding the body.

Deployed at echo.rslv.xyz

Example:

```shell
curl "https://echo.rslv.xyz/some/fake/path?and=query&foo=bar"
{
  "url": "https://echo.rslv.xyz/some/fake/path?and=query&foo=bar", 
  "method": "GET", 
  "path": "some/fake/path", 
  "query": {
    "and": "query", 
    "foo": "bar"
  }, 
  "headers": {
    "accept": "*/*", 
    "forwarded": "for=24.126.83.201;host=echo.rslv.xyz;proto=https;sig=0QmVhcmVyIGM3YTdjZTlmOWYyZmMzNWYzOTBiNjExNTkzZjA2MGU2OGFhZDY4NzgxYzczZTdlODUxMTI1NzE4NWQyMTA1OWM=;exp=1711976059", 
    "host": "echo.rslv.xyz", 
    "user-agent": "curl/8.4.0", 
    "x-forwarded-for": "24.126.83.201", 
    "x-forwarded-host": "echo.rslv.xyz", 
    "x-forwarded-proto": "https", 
    "x-real-ip": "24.126.83.201"
  }
}
```