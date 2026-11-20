using System;
using Microsoft.AspNetCore.Mvc;

namespace WebApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class Putcontroller1 : ControllerBase
    {

        [HttpPut("Put1")]
        public IActionResult Put(int id)
        {
            return NoContent();
        }
    }
}