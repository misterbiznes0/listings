public function index()
{
    $appointments = Appointment::with(['service', 'queueTicket'])
        ->where('user_id', Auth::id())
        ->latest()
        ->get();

    return view('appointments.index', compact('appointments'));
}
