def calculate_voxel_position(x, y, z):
    """ボクセル座標を計算"""
    return x, y, z


def calculate_voxel_position_from_world_position(world_x, world_y, world_z, chunk_size=16):
    """ワールド座標からボクセル座標を計算"""
    voxel_x = int(world_x // chunk_size)
    voxel_y = int(world_y // chunk_size)
    voxel_z = int(world_z // chunk_size)
    return voxel_x, voxel_y, voxel_z


# テストコード
if __name__ == "__main__":
    import unittest
    
    class TestVoxelCalculations(unittest.TestCase):
        def test_calculate_voxel_position(self):
            """calculate_voxel_positionのテスト"""
            x, y, z = calculate_voxel_position(1, 2, 3)
            self.assertEqual(x, 1)
            self.assertEqual(y, 2)
            self.assertEqual(z, 3)
            
        def test_calculate_voxel_position_from_world_position(self):
            """calculate_voxel_position_from_world_positionのテスト"""
            # チャンクサイズ16の場合
            voxel_x, voxel_y, voxel_z = calculate_voxel_position_from_world_position(32, 48, 16)
            self.assertEqual(voxel_x, 2)
            self.assertEqual(voxel_y, 3)
            self.assertEqual(voxel_z, 1)
            
            # 負の座標のテスト
            voxel_x, voxel_y, voxel_z = calculate_voxel_position_from_world_position(-16, -32, -48)
            self.assertEqual(voxel_x, -1)
            self.assertEqual(voxel_y, -2)
            self.assertEqual(voxel_z, -3)
            
            # カスタムチャンクサイズのテスト
            voxel_x, voxel_y, voxel_z = calculate_voxel_position_from_world_position(50, 100, 150, chunk_size=10)
            self.assertEqual(voxel_x, 5)
            self.assertEqual(voxel_y, 10)
            self.assertEqual(voxel_z, 15)
    
    unittest.main()
