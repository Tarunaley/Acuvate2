using Microsoft.AspNetCore.Mvc;
namespace Webapi.Controllers{
    [ApiController]
    [Route("[Controller]")]
    public class CreateGetreq : ControllerBase
    {
        [HttpGet]
        public string Get()
        {
            return "Get created my prasanth";
        }
        }
    }
