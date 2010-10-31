(function(){

	var timer_interval,
	    days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday'],
            months_of_the_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
		                  'September', 'October', 'November', 'December'];

	var timer = {
		init: function()
		{
			timer_interval = setInterval(timer.update, 1000);
		},
		update: function()
		{
			var timer_element = document.getElementById('timer'),
			    current_date = new Date(),
			    hour_data = timer.twelve_hour_format(current_date.getHours()),
			    date_string;

			date_string = days_of_the_week[current_date.getDay()] + ', '
			            + months_of_the_year[current_date.getMonth()] + ' '
			            + timer.get_readable_date(current_date.getDate()) + ' '
			            + hour_data[0] + ':'
			            + timer.digit_trail(current_date.getMinutes()) + ':'
			            + timer.digit_trail(current_date.getSeconds()) + ' '
			            + hour_data[1];

			timer_element.innerHTML = date_string;
		},
		digit_trail: function(n, count)
		{
			count = count || 2;
			n = n.toString();

			if (n.length >= count)
				return n;

			for (var i=n.length; i < count; ++i)
				n = '0' + n;

			return n;
		},
		get_readable_date: function(d)
		{
			d_str = d.toString();

			if (d > 10 && d < 14)
				return d_str + 'th';

			if (d_str[d_str.length-1] == '1')
				return d_str + 'st';

			if (d_str[d_str.length-1] == '2')
				return d_str + 'nd';

			if (d_str[d_str.length-1] == '3')
				return d_str + 'rd';

			return d_str + 'th';
		},
		twelve_hour_format: function(h)
		{
			var segment = 'AM';

			if (h > 12)
			{
				h = h - 12;
				segment = 'PM';
			}

			return [h, segment];
		}
	};

	window.timer = window.timer || timer;

	if (window.all) window.attachEvent('load', timer.init);
	else window.addEventListener('load', timer.init, false);

})();
