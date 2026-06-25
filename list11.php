public function create()
{
    $services = Service::all();

    return view('appointments.create', compact('services'));
}
