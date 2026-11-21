using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace WebApi.Controllers
{
    [Route("[controller]")]
    public class deleteapi3 : Controller
    {
        private readonly ILogger<deleteapi3> _logger;

        public deleteapi3(ILogger<deleteapi3> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            Console.WriteLine("Main branch");
            return View("Error!");
        }
    }
}
