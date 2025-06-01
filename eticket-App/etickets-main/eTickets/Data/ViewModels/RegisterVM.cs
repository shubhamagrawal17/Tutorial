using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace eTickets.Data.ViewModels
{
    public class RegisterVM
    {
        [Display(Name = "Name and surname")]
        [Required(ErrorMessage = "First and last name is required.")]
        public string FullName { get; set; }

        [Display(Name = "Email Address")]
        [Required(ErrorMessage = "Email Address is required.")]
        public string EmailAddress { get; set; }

        [Display(Name = "Password")]
        [Required]
        [StringLength(50, MinimumLength = 8, ErrorMessage = "Your password must be a minimum of 8 characters.")]
        [RegularExpression("^((?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])|(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[^a-zA-Z0-9])|(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[^a-zA-Z0-9])|(?=.*?[a-z])(?=.*?[0-9])(?=.*?[^a-zA-Z0-9])).{8,}$", ErrorMessage = "The password must be at least 8 characters and contain one uppercase letter, one lowercase letter, one number, and one special character: uppercase letters (A-Z), lowercase letters (a-z), numbers (0-9) and special charactersr (ör. !@#$%^&*)")]
        [DataType(DataType.Password)]
        public string Password { get; set; }

        [Display(Name = "Password Confirmation")]
        [Required(ErrorMessage = "Password Confirmation Required.")]
        [DataType(DataType.Password)]
        [Compare("Password", ErrorMessage = "Passwords Don't Match")]
        public string ConfirmPassword { get; set; }
    }
}
