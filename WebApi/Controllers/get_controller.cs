
using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class GetController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok("Hello! Welcome to my first API.");
    }
}
