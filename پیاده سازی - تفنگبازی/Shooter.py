class Shooter:
    weapons = {'Submachine Gun': [100, 10, 0.5, 1], 'Assault Rifle': [200, 20, 1, 1.5], 'Pistol': [80, 8, 0.5, 1], 'Shotgun': [50, 40, 4.0, 2], 'Sniper Rifle': [1000, 30, 3.0, 3]}

    def __init__(self):
        self.name = None
        self.count = 0

    def set_gun_by_name(self, name: str) -> None:
        if name not in Shooter.weapons.keys():
            raise ValueError('Invalid gun name')
        else:
            self.name = name

    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None:
        if self.name is None:
            raise ValueError('Gun is not set')
        else:
            if Shooter.weapons[self.name][2] != size:
                raise ValueError('Invalid gun or bullet size')

        if count < 0:
            raise ValueError('Invalid bullet count')
        else:
            self.count += count

        if size not in [weapon[2] for weapon in Shooter.weapons.values()]:
            raise ValueError('Invalid bullet size')


    def shoot_to_target(self, target_x: int,  target_y: int,  target_distance: int,  aim_x: int,  aim_y: int) -> int:
        if self.count <= 0:
            raise ValueError('Invalid bullet')

        if Shooter.weapons[self.name][0] < target_distance:
            return 0
        if target_x < aim_x < target_x + 10 and target_y < aim_y < target_y + 10:
            self.count -= 1
            return Shooter.weapons[self.name][1] * Shooter.weapons[self.name][-1]
        else:
            return 0
