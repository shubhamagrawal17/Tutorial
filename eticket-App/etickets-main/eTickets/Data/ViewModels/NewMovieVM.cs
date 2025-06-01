using eTickets.Data;
using eTickets.Data.Base;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Threading.Tasks;

namespace eTickets.Models
{
    public class NewMovieVM
    {
        public int Id { get; set; }

        [Display(Name = "Film Adı")]
        [Required(ErrorMessage = "Film Adı gereklidir.")]
        public string Name { get; set; }

        [Display(Name = "Film Açıklaması")]
        [Required(ErrorMessage = "Açıklama gereklidir.")]
        public string Description { get; set; }

        [Display(Name = "Fiyat ₺")]
        [Required(ErrorMessage = "Fiyat gereklidir.")]
        public double Price { get; set; }

        [Display(Name = "Film Poster URL")]
        [Required(ErrorMessage = "Film poster URL gereklidir.")]
        public string ImageURL { get; set; }

        [Display(Name = "Film vizyona giriş tarihi")]
        [Required(ErrorMessage = "Film vizyona giriş tarihi gereklidir.")]
        public DateTime StartDate { get; set; }

        [Display(Name = "Film vizyon bitiş tarihi")]
        [Required(ErrorMessage = "Film vizyon bitiş tarihi gereklidir.")]
        public DateTime EndDate { get; set; }

        [Display(Name = "Bir film kategorisi seçiniz")]
        [Required(ErrorMessage = "Film kategorisi gereklidir.")]
        public MovieCategory MovieCategory { get; set; }

        //Relationships
        [Display(Name = "Aktör veya Aktörleri seçiniz")]
        [Required(ErrorMessage = "Aktör gereklidir.")]
        public List<int> ActorIds { get; set; }

        [Display(Name = "Sinema salonu seçiniz")]
        [Required(ErrorMessage = "Sinema salonu gereklidir.")]
        public int CinemaId { get; set; }

        [Display(Name = "Yönetmen seçiniz.")]
        [Required(ErrorMessage = "Yönetmen gereklidir.")]
        public int ProducerId { get; set; }
    }
}
