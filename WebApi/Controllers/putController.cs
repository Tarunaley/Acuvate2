
using Microsoft.AspNetCore.Mvc;

namespace MyWebApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class UserController : ControllerBase
    {
        [HttpPut]
        public IActionResult UpdateName(int id, string name)
        {
            return Ok($"User {id} name updated to {name}");
        }
    }
}
