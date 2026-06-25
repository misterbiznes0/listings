public function ticket(Appointment $appointment)
{
    if ($appointment->user_id !== Auth::id()) {
        abort(403);
    }

    $appointment->load(['service', 'queueTicket', 'user']);

    return view('appointments.ticket', compact('appointment'));
}
