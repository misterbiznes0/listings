<select name="service_id" required>
    @foreach($services as $service)
        <option value="{{ $service->id }}">
            {{ $service->name }} — {{ $service->duration_min }} мин.
        </option>
    @endforeach
</select>
