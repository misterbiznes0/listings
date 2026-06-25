public function cancel(Appointment $appointment)
{
    if ($appointment->user_id !== Auth::id()) {
        abort(403);
    }

    $appointment->update(['status' => 'cancelled']);

    if ($appointment->queueTicket) {
        $appointment->queueTicket->update(['status' => 'cancelled']);
    }

    return back()->with('success', 'Запись отменена.');
}
