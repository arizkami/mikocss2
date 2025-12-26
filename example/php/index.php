<?php
// Configuration / Mock Data
$appTitle = "MikoCSS";
$appVersion = "1.0.0";

// Navigation Links
$navItems = [
    'Colors' => '#colors',
    'Layout' => '#layout',
    'Typography' => '#typography',
    'Components' => '#components',
    'Animations' => '#animations',
    'Forms' => '#forms'
];

// Mock Data for Table
$users = [
    ['id' => 1, 'name' => 'John Doe', 'email' => 'john@example.com', 'status' => 'Active', 'color' => 'c32'],
    ['id' => 2, 'name' => 'Jane Smith', 'email' => 'jane@example.com', 'status' => 'Pending', 'color' => 'c48'],
    ['id' => 3, 'name' => 'Bob Johnson', 'email' => 'bob@example.com', 'status' => 'Inactive', 'color' => 'c1'],
];

// Mock Data for Colors (Simulating the 524 color palette)
$spectra = [
    'Red Spectrum (c1)' => 'c1',
    'Blue Spectrum (c16)' => 'c16',
    'Green Spectrum (c32)' => 'c32',
    'Yellow Spectrum (c48)' => 'c48'
];

$buttonTypes = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark'];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $appTitle; ?> - Complete Feature Demo</title>
    <link rel="stylesheet" href="cogeden.css">
    <style>
        .demo-section { margin-bottom: 48px; }
        .demo-box { padding: 16px; margin: 8px 0; }
        .color-swatch { width: 80px; height: 80px; display: inline-block; margin: 4px; border-radius: 4px; }
        /* Custom overrides for demo purposes */
        .bg-scheme-primary { background-color: #ffffff; }
        .text-scheme-primary { color: #1f2937; }
        .bg-scheme-secondary { background-color: #f3f4f6; }
        .text-scheme-secondary { color: #6b7280; }
        .bg-scheme-tertiary { background-color: #e5e7eb; }
        .border-scheme { border-color: #d1d5db; }
        
        /* Dark mode overrides would go here via JS class toggling */
    </style>
</head>
<body class="bg-scheme-primary text-scheme-primary">
    
    <header class="bg-scheme-secondary border-b border-scheme">
        <div class="container"> <div class="flex items-center justify-between py-4 px-4">
                <div>
                    <h1 class="text-3xl font-bold"><?php echo $appTitle; ?></h1>
                    <p class="text-sm text-scheme-secondary">PHP Dynamic Demonstration</p>
                </div>
                <div id="theme-toggle">
                    <button class="btn btn-sm btn-secondary">Toggle Theme</button>
                </div>
            </div>
        </div>
    </header>

    <nav class="bg-scheme-tertiary border-b border-scheme">
        <div class="container">
            <ul class="flex list-none p-0 m-0">
                <?php foreach($navItems as $label => $link): ?>
                    <li><a href="<?php echo $link; ?>" class="text-scheme-primary p-4 inline-block font-bold" style="text-decoration:none;"><?php echo $label; ?></a></li>
                <?php endforeach; ?>
            </ul>
        </div>
    </nav>

    <main class="container py-8 px-4">
        
        <section id="colors" class="demo-section">
            <h2 class="text-2xl font-bold mb-6">524 Color Palette System</h2>
            
            <div class="bg-scheme-secondary rounded shadow-scheme p-6 mb-6">
                <h3 class="text-xl font-semibold mb-4">Neutral Colors</h3>
                <div class="flex flex-wrap">
                    <div class="color-swatch bg-black"></div>
                    <div class="color-swatch bg-white border"></div>
                    <?php 
                    // Generating Grays 100-900
                    for($i=1; $i<=9; $i++): ?>
                        <div class="color-swatch bg-gray-<?php echo $i; ?>00"></div>
                    <?php endfor; ?>
                </div>
            </div>

            <div class="bg-scheme-secondary rounded shadow-scheme p-6 mb-6">
                <h3 class="text-xl font-semibold mb-4">Color Wheel Samples</h3>
                <div class="row">
                    <?php foreach($spectra as $label => $code): ?>
                    <div class="col-3" style="width: 25%; float: left;">
                        <h4 class="font-semibold mb-2"><?php echo $label; ?></h4>
                        <div class="flex flex-wrap">
                            <?php 
                            // Dynamically generate shades 100-800
                            for($s=100; $s<=800; $s+=100): 
                            ?>
                                <div class="color-swatch bg-<?php echo $code; ?>-<?php echo $s; ?>" title=".bg-<?php echo $code; ?>-<?php echo $s; ?>"></div>
                            <?php endfor; ?>
                        </div>
                    </div>
                    <?php endforeach; ?>
                    <div class="clearfix"></div>
                </div>
            </div>
        </section>

        <section id="layout" class="demo-section">
            <h2 class="text-2xl font-bold mb-6">Grid System</h2>
            <div class="bg-scheme-secondary rounded shadow-scheme p-6 mb-6">
                <div class="row mb-4">
                    <div class="col-4 float-left w-half p-2">
                        <div class="bg-c16-400 text-white p-4 rounded text-center">Span 4</div>
                    </div>
                    <div class="col-4 float-left w-half p-2">
                        <div class="bg-c32-400 text-white p-4 rounded text-center">Span 4</div>
                    </div>
                    <div class="col-4 float-left w-half p-2">
                        <div class="bg-c48-400 text-white p-4 rounded text-center">Span 4</div>
                    </div>
                    <div class="clearfix"></div>
                </div>
            </div>
        </section>

        <section id="components" class="demo-section">
            <h2 class="text-2xl font-bold mb-6">UI Components</h2>
            
            <div class="bg-scheme-secondary rounded shadow-scheme p-6 mb-6">
                <h3 class="text-xl font-semibold mb-4">Buttons</h3>
                <div class="flex flex-wrap">
                    <?php foreach($buttonTypes as $btn): ?>
                        <button class="btn btn-<?php echo $btn; ?> m-2 p-2 border rounded capitalize">
                            <?php echo $btn; ?>
                        </button>
                    <?php endforeach; ?>
                </div>
            </div>

            <div class="bg-scheme-secondary rounded shadow-scheme p-6">
                <h3 class="text-xl font-semibold mb-4">Dynamic Table</h3>
                <table class="w-full text-left border-collapse">
                    <thead>
                        <tr class="border-b border-gray-300">
                            <th class="p-2">ID</th>
                            <th class="p-2">Name</th>
                            <th class="p-2">Email</th>
                            <th class="p-2">Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php foreach($users as $user): ?>
                        <tr class="border-b border-gray-200">
                            <td class="p-2"><?php echo $user['id']; ?></td>
                            <td class="p-2"><?php echo $user['name']; ?></td>
                            <td class="p-2"><?php echo $user['email']; ?></td>
                            <td class="p-2">
                                <span class="bg-<?php echo $user['color']; ?>-500 text-white px-2 py-1 rounded text-sm">
                                    <?php echo $user['status']; ?>
                                </span>
                            </td>
                        </tr>
                        <?php endforeach; ?>
                    </tbody>
                </table>
            </div>
        </section>

        <section id="animations" class="demo-section">
            <h2 class="text-2xl font-bold mb-6">Animations</h2>
            <div class="bg-scheme-secondary rounded shadow-scheme p-6">
                <div class="flex justify-between">
                    <div class="text-center p-4">
                        <div class="bg-c16-400 text-white p-6 rounded animate-pulse inline-block">Pulse</div>
                    </div>
                    <div class="text-center p-4">
                         <div class="inline-block w-12 h-12 border-4 border-c32-500 border-t-transparent rounded-full animate-spin"></div>
                    </div>
                    <div class="text-center p-4">
                        <div class="bg-c1-500 text-white p-6 rounded animate-bounce inline-block">Bounce</div>
                    </div>
                </div>
            </div>
        </section>

    </main>

    <footer class="bg-scheme-secondary border-t border-scheme py-8 mt-12">
        <div class="container text-center px-4">
            <p class="text-scheme-secondary">&copy; <?php echo date("Y"); ?> <?php echo $appTitle; ?>. Generated with Python & PHP.</p>
        </div>
    </footer>

</body>
</html>