$appointment = Appointment::create([
    'user_id' => Auth::id(),
    'service_id' => $request->service_id,
    'appointment_time' => $request->appointment_time,
    'status' => 'pending',
]);
