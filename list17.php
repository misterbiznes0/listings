'appointment_time' => [
    'required',
    'date',
    'after:now',
    function ($attribute, $value, $fail) {
        $hour = date('H', strtotime($value));

        if ($hour < 9 || $hour >= 18) {
            $fail('Запись доступна только с 09:00 до 18:00.');
        }
    },
],
