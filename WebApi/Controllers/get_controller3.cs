using Microsoft.AspNetCore.Mvc;

namespace StudentApi.Controllers
{
    [ApiController]
    [Route("Hello")]
    public class HelloController : ControllerBase
    {
        [HttpGet]
        public ActionResult<string> Get()
        {
            return Ok("Hello,welcome to ASP.NET Core Web API!");
        }
    }
}