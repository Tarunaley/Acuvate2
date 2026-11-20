using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class Get_controller : ControllerBase
{
    [HttpGet]
    public IActionResult getapp()
    {
        return Ok("GET API is working");
    }
}