using Microsoft.AspNetCore.Mvc;
 
[ApiController]
[Route("api/[controller]")]
public class Post_controller : ControllerBase
{
    [HttpPost]
    public IActionResult postapp()
    {
        return Ok("POST API is working");
    }
}