using eTickets.Data.Base;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace eTickets.Models
{
    public class Producer:IEntityBase
    {
        [Key]
        public int Id { get; set; }

        [Display(Name = "Profil Resmi")]
        [Required(ErrorMessage = "Profil resmi gereklidir.")]
        public string ProfilePictureURL { get; set; }

        [Display(Name = "Ad ve Soyad")]
        [Required(ErrorMessage = "Ad ve Soyad gereklidir.")]
        [StringLength(50, MinimumLength = 3, ErrorMessage = "Ad ve Soyad 3 ile 50 karakter arasında olmalıdır.")]
        public string FullName { get; set; }

        [Display(Name = "Biyografi")]
        [Required(ErrorMessage = "Biyografi gereklidir.")]
        public string Bio { get; set; }

        //Relationships
        public List<Movie> Movies { get; set; }
    }
}
