def solution(bandage, health, attacks):
    cast_time, heal_per_sec, extra_heal = bandage

    max_health = health
    current_health = health

    attack_ptr = 0
    total_attacks = len(attacks)

    continuous_time = 0
    final_time = attacks[-1][0]

    for second in range(1, final_time + 1):
        # 공격이 있는 초
        if attack_ptr < total_attacks and attacks[attack_ptr][0] == second:
            damage = attacks[attack_ptr][1]
            current_health -= damage
            continuous_time = 0
            attack_ptr += 1

            if current_health <= 0:
                return -1
        else:
            # 붕대 감기
            continuous_time += 1
            current_health = min(max_health, current_health + heal_per_sec)

            if continuous_time == cast_time:
                current_health = min(max_health, current_health + extra_heal)
                continuous_time = 0

    return current_health
