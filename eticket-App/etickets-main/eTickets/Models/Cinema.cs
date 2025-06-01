using eTickets.Data.Base;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace eTickets.Models
{
    public class Cinema:IEntityBase
    {
        [Key]
        public int Id { get; set; }

        [Display(Name = "Sinema Logo")]
        [Required(ErrorMessage = "Sinema Logo gereklidir.")]
        public string Logo { get; set; }

        [Display(Name = "Sinema Adı")]
        [Required(ErrorMessage = "Sinema Adı gereklidir.")]
        public string Name { get; set; }

        [Display(Name = "Sinema Hakkında")]
        [Required(ErrorMessage = "Sinema Hakkında kısmı gereklidir.")]
        public string Description { get; set; }

        //Relationships
        public List<Movie> Movies { get; set; }
    }
}
