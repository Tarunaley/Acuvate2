using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class DemoController : ControllerBase
{
    [HttpDelete("{id}")]
    public IActionResult Delete(int id)
    {
        return Ok($"Deleted item {id}");
    }
}