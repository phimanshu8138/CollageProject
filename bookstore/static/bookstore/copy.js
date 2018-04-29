// JavaScript Document
$(document).ready(function(e) {

	/// Tab Content Start
	$('.left-section li').click(function(){

		  /// Remove Class
		   $('li').removeClass('active-tab-menu');
		   $('.content-box').removeClass('active-content');

		  // Add Class
		  $(this).addClass('active-tab-menu');
		  var getTabMenuClass = $(this).attr('class').split(' ')[0];
		  $('.'+getTabMenuClass+'-content').addClass('active-content');

		  /// Hide Next And Previous
           if(getTabMenuClass=='form-step-1')
		   {
			  $('.previous-section').addClass('Hide-this');
			  $('.next-section').removeClass('Hide-this');
		   }
		   else if(getTabMenuClass=='form-step-5')
		   {
			  $('.next-section').addClass('Hide-this');
			  $('.previous-section').removeClass('Hide-this');
		   }
		   else
		   {
			   $('.previous-section').removeClass('Hide-this');
			   $('.next-section').removeClass('Hide-this');

		   }



		})

	/// Tab Content End here

	/// NEXT SECTION
	$('.next-section').click(function(){

		if($('li').hasClass('active-tab-menu'))
		{
			/// Tab Menu
		   $('.active-tab-menu').next().addClass('active-tab-menu-new');
		   $('.active-tab-menu-new').prev().removeClass('active-tab-menu');
		   // Tab Content
		   $('.active-content').next().addClass('active-content-new');
		   $('.active-content-new').prev().removeClass('active-content');
		}
		else
		{
			/// Tab Menu
		   $('.active-tab-menu-new').next().addClass('active-tab-menu');
		   $('.active-tab-menu').prev().removeClass('active-tab-menu-new');
		   // Tab Conten
		   $('.active-content-new').next().addClass('active-content');
		   $('.active-content').prev().removeClass('active-content-new');
		}

		});

	/// NEXT SECTION END

	/// PREVIOUS SECTION
	$('.previous-section').click(function(){

		if($('li').hasClass('active-tab-menu'))
		{
			/// Tab Menu
		   $('.active-tab-menu').prev().addClass('active-tab-menu-new');
		   $('.active-tab-menu-new').next().removeClass('active-tab-menu');
		   // Tab Content
		   $('.active-content').prev().addClass('active-content-new');
		   $('.active-content-new').next().removeClass('active-content');
		}
		else
		{
			/// Tab Menu
		   $('.active-tab-menu-new').prev().addClass('active-tab-menu');
		   $('.active-tab-menu').next().removeClass('active-tab-menu-new');
		   // Tab Conten
		   $('.active-content-new').prev().addClass('active-content');
		   $('.active-content').next().removeClass('active-content-new');
		}

		});

	/// NEXT SECTION END




});