public function adminQueue()
{
    $appointments = Appointment::with(['user', 'service', 'queueTicket'])
        ->orderBy('appointment_time')
        ->get();

    return view('admin.queue', compact('appointments'));
}
