function clockAngle(time) {
    const [hh, mm] = time.split(":").map(Number);

    const hour = hh % 12;

    const minuteAngle = 6 * mm;
    const hourAngle = 30 * hour + 0.5 * mm;

    let angle = Math.abs(hourAngle - minuteAngle);
    angle = Math.min(angle, 360 - angle);

    return Math.round(angle);
}